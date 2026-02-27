# Fatigue Analysis

**Category:** Materials & Failure
**Tags:** fatigue, S-N curve, endurance, stress

---

Fatigue failure occurs when a material is subjected to repeated loading and unloading cycles, even at stress levels well below the static yield strength.

## S-N Curve (Wohler Curve)

The relationship between stress amplitude (S) and number of cycles to failure (N):

- Plot log(S) vs log(N) from experimental data
- Steel typically shows an endurance limit (S_e) below which infinite life is expected
- Aluminum and most non-ferrous metals have no true endurance limit

## Endurance Limit Estimation (Steel)

S_e' = 0.5 * S_ut (for S_ut < 200 ksi / 1400 MPa)
S_e' = 100 ksi / 700 MPa (for higher strengths)

## Modified Endurance Limit

S_e = k_a * k_b * k_c * k_d * k_e * S_e'

- k_a = Surface factor (machined: 0.7-0.9, ground: 0.9-1.0)
- k_b = Size factor (smaller parts are stronger)
- k_c = Load factor (bending: 1.0, axial: 0.85, torsion: 0.59)
- k_d = Temperature factor
- k_e = Reliability factor (50%: 1.0, 99%: 0.814, 99.9%: 0.753)

## Goodman Criterion (Mean + Alternating Stress)

sigma_a / S_e + sigma_m / S_ut = 1/n

- sigma_a = Alternating stress amplitude
- sigma_m = Mean stress
- n = Factor of safety

## Miner's Rule (Cumulative Damage)

D = sum(n_i / N_i) = 1 at failure

Where n_i is cycles at stress level i, and N_i is the life at that stress level.
