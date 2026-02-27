# Bolted Joints

**Category:** Fasteners
**Tags:** bolts, joints, preload, torque

---

Bolted joints are one of the most common methods of mechanical assembly. Proper bolt preload is critical for joint reliability.

## Torque-Preload Relationship

T = K * F * d

- T = Applied torque (N-m or ft-lbf)
- K = Nut factor (typically 0.15-0.20 for dry, 0.12-0.15 for lubricated)
- F = Desired preload force (N or lbf)
- d = Nominal bolt diameter (m or ft)

## Recommended Preload

For most applications, preload should be 75-90% of the bolt proof load:

F_preload = 0.75 * S_proof * A_tensile

- S_proof = Bolt proof strength (from grade tables)
- A_tensile = Tensile stress area of the bolt

## Common Bolt Grades

- **Grade 5 (SAE):** S_proof = 85 ksi, S_tensile = 120 ksi
- **Grade 8 (SAE):** S_proof = 120 ksi, S_tensile = 150 ksi
- **Class 8.8 (Metric):** S_proof = 580 MPa, S_tensile = 800 MPa
- **Class 10.9 (Metric):** S_proof = 830 MPa, S_tensile = 1040 MPa

## Joint Separation

A joint will separate when the external load exceeds:

F_sep = F_preload * (1 + C) / C

Where C is the joint stiffness ratio (bolt stiffness / total stiffness).
