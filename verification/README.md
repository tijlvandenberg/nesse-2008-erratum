# Verification

Twee Python-bestanden:

- **`nesse_polynomial.py`** — stand-alone implementatie van de 6e-graads
  Nesse-polynomen voor alle 14 tandtypes, met de gecorrigeerde a₅ voor
  max #2. Geen externe dependencies behalve de standard-library. Snel
  cli-demo via `python3 nesse_polynomial.py`.
- **`test_nesse_coef.py`** — pytest-suite die 25 ankerpunten uit
  Nesse Fig 2a–c verifieert binnen 0.5 mm² / 1 % tolerantie + specifieke
  typo-kanarie. Draaien met `python3 -m pytest test_nesse_coef.py -v`
  (vergt pytest).

Beide zijn MIT-licentie; je mag ze hergebruiken in je eigen PISA-tools.
