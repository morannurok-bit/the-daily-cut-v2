# Fit Matching Model — Closeness & Scale (The Daily Cut)

How the engine decides whether a garment's **fit** (closeness to the body) and **scale** (cut for the wearer's height) work for a given woman. This sits in the matching pipeline *after* intent classification and body-type filtering, and *before* final scoring. Two independent models live here: **closeness** and **scale**. Each returns either a hard gate (item removed) or a soft factor/penalty that feeds the score.

Both models share one governing idea, learned the hard way through real try-ons: **a single tag is not enough to know how a garment behaves on the body.** Closeness depends on the fabric and the cut, not just the label; scale depends on what tailoring can and can't fix. The models below encode that.

---

## 1. Closeness Model

### 1.1 The ladder and the two kinds of boundary

Closeness runs on a four-rung ladder:

```
tight (0)  <  close (1)  <  relaxed (2)  <  oversized (3)
```

The key insight is that these four rungs are **not** four equal points on a line — they split into two categories:

- **The extremes — `tight` and `oversized` — are deliberate looks.** A woman either wants body-hugging, or she wants to be swallowed by fabric; there's no ambiguity. If she didn't choose an extreme, an item at that extreme is *wrong* for her, not merely a near-miss.
- **The middle — `close` and `relaxed` — is ambiguous.** "Close" and "relaxed" blur into each other: jeans come close by default, a fitted-but-not-tight top reads either way, structure changes everything. A woman leaning one way still wears the other sometimes.

This produces the core rule:

> **Extremes gate; the middle penalizes.**

If an item sits at an extreme the woman did not choose (`tight` when she didn't pick tight, `oversized` when she didn't pick oversized), it is **hard-gated** — removed. If an item sits in the middle and doesn't match her pick, it is a **distance penalty** — present, ranked lower, never removed.

The `tight` gate is also the **bodycon firewall**: a woman who chose "close, but not tight" is gated away from anything tagged `tight`. The `oversized` gate is its mirror: a woman who wants room "with a little ease" isn't handed a garment she'll drown in.

### 1.2 Distance and direction

Both regions of a garment are checked — **top** (her top-closeness pick vs. the item's `closeness_top`) and **bottom** (her bottom pick vs. `closeness_bottom`). The **worst region drives** the outcome: if either region gates, the item gates; otherwise the larger of the two distance penalties applies.

For a middle mismatch, distance is the number of rungs from the item's value to her nearest chosen value, capped at 2. That distance feeds the strong-preference penalty table (see §3), so how hard it bites depends on her permissiveness dial.

This replaced an earlier, wrong model that treated the axis as "tighter-than-chosen gates, looser-than-chosen penalizes." The real axis is **extreme vs. middle**, not tighter vs. looser.

### 1.3 Fabric modifier — body-following fabric tightens the read

A `close` tag understates a garment that *follows* the body. A close rib tee that skims, or anything that clings, reads as body-conscious as something a rung tighter. So:

> A `close` item in a **body-following fabric** (fabric behavior contains *skim* or *cling*) is treated like an extreme: it **gates** for anyone who did not choose `close`-or-tighter.

A relaxed-seeker is therefore ruled out of a skimming close tee — it shows the body she asked to keep easy. A close-seeker still gets it (she chose close; the skim is what she wants). The gate only fires against people who didn't ask for close.

### 1.4 Cut modifier — a grip-and-expand cut releases the read

The mirror image. A `close` tag *overstates* a garment that grips at the waist and then flares away from the body. An A-line skirt or a fit-and-flare dress is fitted at the waist and seat but releases over the hips and legs — it skims the very zone `close` implies it hugs. So:

> A `close` item with a **grip-and-expand silhouette** (silhouette contains *a_line* or *fit_flare*) **also serves `relaxed`**: its `close` reading expands to include `relaxed`, so it matches relaxed-seekers as well as close-seekers.

The garment stays honestly tagged `close` (it *does* grip at the waist); the engine understands the cut releases below. The grip itself isn't a closeness penalty — it's the waist event, which belongs to Intent 2. This modifier applies to the **bottom region only** (a fit-flare dress's bodice stays honestly close; only its skirt releases).

### 1.5 The zone principle underneath both modifiers

The fabric and cut modifiers are two faces of one truth: **a bottom's closeness is really two zones — the waist/seat grip and the leg/body room — and the closeness tag describes the leg/body room.** The waist grip is captured separately as the waist event (Intent 2). This is why "fitted at the waist and seat, but relaxed in the leg" is a coherent, common preference (a woman can give us both signals without contradiction), and why a grip-and-expand cut satisfies a relaxed-seeker: its leg/body *is* relaxed.

### 1.6 Tagging discipline for closeness

- **Bodycon, clinging, or ruched garments are tagged `tight`, never `close`.** This is what makes "close, but not tight" a real firewall.
- **Tag closeness to the garment's actual fit.** A grip-and-expand piece is honestly `close` at the waist; the engine's cut modifier handles the release. Do not pre-soften it to `relaxed` in the data — let the model reason.
- Fabric behavior (`skim` / `cling` vs. `structured` / `drape`) must be tagged accurately, because the closeness read depends on it.

---

## 2. Scale Model

### 2.1 Tiers and bands

Height runs on four tiers:

```
petite (0)  <  mid_short (1)  <  mid_tall (2)  <  tall (3)
```

Each item carries a **scale band** — the set of tiers its cut and proportions flatter (e.g. `mid_short_friendly, mid_tall_friendly, tall_friendly`). A band is a range, not a point: the garment works across the tiers it's tagged for. A `_required` suffix marks a band as strict (no tolerance).

If the wearer's tier is **in the band**, it's a full match (factor 1.0).

### 2.2 Tolerance is downward-only

You can shorten a garment; you cannot lengthen one. So tolerance is asymmetric:

- **Too short (wearer taller than the band):** hard gate, always. There is no upward notch, ever — you can't add length that isn't there. A `tall_required` or any item whose band tops out below the wearer is simply out.
- **Too long (wearer shorter than the band):** tolerated, because the excess can be taken in — but how much, and at what cost, depends on the garment and the wearer (below).

Beyond two tiers of "too long" (distance ≥ 3), everything gates — the alteration is too large to rescue the proportions.

### 2.3 Length-critical garments (pants and midi+ dresses/skirts)

For garments where length is structural:

- **Hemmable pants** — full-length pants in a **straight-profile cut** (`slim`, `straight`, `cigarette`→slim, `mom_fit`, `wide`) hem cleanly, because shortening doesn't change the leg's shape. They get a hemming notch: **one tier → 0.85, two tiers → 0.65** (the bigger alteration is the bigger compromise). Hemming is *baseline* — it is **not** gated by the permissiveness dial; even a restrictive petite woman can hem.
  - **Petite cap:** petite (tier 0) gets **one tier of hemming only**. A two-tier-taller pant is gated for petite, because hemming fixes the hem but not the **rise** — a pant graded for mid-tall has a long rise that sits at a petite woman's ribs, and no amount of hemming corrects that. The middle tiers (mid_short, mid_tall) have enough proportional margin to absorb a two-tier hem; petite does not. (This is exactly the line between a mid-short woman successfully hemming a tall wide-leg, and a petite woman being handed a mid-tall trouser that won't sit right.)
- **Shaped-leg pants** (`flared`, `bootcut`, `barrel`) are **not** hemmable — the hem width is part of the design — so too-long is strict (gate).
- **Midi-and-longer dresses and skirts** are length-critical and **strict** — shortening a midi changes its character. (A mini/short dress is not length-critical and falls under §2.4.)

### 2.4 Non-length-critical garments

- **Tops** (hip- or waist-length) are length-lenient: a too-long top tucks in or simply sits a little longer. One tier too tall → **0.9**, not gated; two-plus tiers → gate. This leniency is *not* permissiveness-gated — anyone can tuck or wear a top slightly long, so even a restrictive woman gets it.
- **Other forgiving garments** (relaxed, drapey pieces with slack to absorb size) get a one-tier notch at **0.8**, but only for a **non-restrictive** wearer — here the permissiveness dial does apply, because absorbing extra size is a genuine compromise a picky woman won't make.
- Everything else, too-long, is strict.

### 2.5 What scale returns

`scale_match` returns `(ok, factor, flags)`: a gate (`ok=False`, item removed), or a factor in {0.65, 0.8, 0.85, 0.9, 1.0} multiplied into the score, with a flag (`hem_to_length`, `top_length_lenient`, `scale_notch`) recording why.

---

## 3. How fit feeds the score

Closeness and scale are both consulted in the pipeline after the body filter:

- **Hard gates** (a closeness extreme/skim gate, a too-short or over-distance scale gate, a cut/length/exposure avoid) remove the item entirely.
- **Closeness middle mismatches** become a **distance** (0–2) fed into the strong-preference penalty table alongside rise, dress/skirt length, and fabric discomfort. These distances **compound** and are **bent by the fit-permissiveness dial**: for a restrictive woman a one-step miss multiplies by ~0.25 and a two-step miss by ~0.05 (misses are buried); for a permissive woman the same misses multiply by ~0.85 and ~0.6 (misses survive). The dial is derived from the woman (styling agency + closeness breadth, nudged by restriction load), never set globally.
- **Scale tolerance** contributes its factor (0.65–0.9) directly.

The net effect: a restrictive, particular woman gets a tight feed of near-exact matches with compromises buried; a flexible woman gets a wide feed where one-step-off pieces still rank well. Same catalog, different feeds — driven entirely by what she told us.

---

## 4. Design history (why the model looks like this)

Every rule here was forced by a real profile, not theorized:

- **Extremes vs. middle** came from the observation that `tight` and `oversized` are conscious choices while `close`/`relaxed` are the ambiguous middle — so the old "tighter gates, looser penalizes" asymmetry was the wrong axis.
- **The skim gate** came from a relaxed-seeker who would have hated a close, body-skimming rib tee — while a close-seeker rightly leads with it.
- **The A-line release** came from the same woman *liking* a close A-line skirt — its structure and cut release where the tee clings.
- **Two-tier hemming** came from a mid-short woman hemming a tall wide-leg and loving it.
- **The petite cap** came from recognizing that what works for mid-short (a two-tier hem) leaves a petite woman with a rise at her ribs.
- **Top leniency** came from a too-tall shirt being a non-issue for anyone who tucks.

The throughline: *closeness and scale are the tag plus how the fabric, the cut, and tailoring behave on the actual body.*

---

End of fit matching model specification.
