# Beam Deflection

**Category:** Structural Analysis
**Tags:** beams, loads, stress, deflection

---

Beam deflection is the degree to which a structural element is displaced under a load. It is a key consideration in the design of beams, bridges, and other structural components.

## Key Formulas

- **Simply supported beam, center point load:**
  delta = PL^3 / 48EI

- **Cantilever beam, end point load:**
  delta = PL^3 / 3EI

- **Simply supported beam, uniform distributed load:**
  delta = 5wL^4 / 384EI

## Variables

- P = Applied load (N or lbf)
- w = Distributed load per unit length (N/m or lbf/ft)
- L = Beam length (m or ft)
- E = Modulus of elasticity (Pa or psi)
- I = Second moment of area (m^4 or in^4)
- delta = Maximum deflection

## Notes

For complex loading, use superposition: calculate deflection for each load case individually and sum the results. This is valid as long as the beam remains in the elastic region.
