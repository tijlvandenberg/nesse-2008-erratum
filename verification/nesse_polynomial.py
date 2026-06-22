"""Stand-alone implementatie van de Nesse 2008 6e-graads polynomen voor
PESA/ALSA-berekening. Geen externe dependencies.

Coëfficiënten zoals gepubliceerd in Nesse W et al. (2008)
J Clin Periodontol 35:668-673, met ÉÉN correctie t.o.v. de gedrukte
Tabel 1: a₅ voor max #2 (laterale incisief boven) staat hier op
0.005890; in de gedrukte tabel staat 0.05890 (decimaal-typo, zie de
Letter to the Editor in ../manuscript/).
"""
import math

# Coëfficiënten per tandtype (laatste FDI-cijfer; 8 → 7 = verstandskies = 2e molaar)
PESA_COEF_MAX = {
    1: (12.3905, 0.1374, 0.6717, -0.14536, 0.01126, -0.0003083),    # centr.incis
    2: (18.7571, -1.6471, 0.5258, -0.07900, 0.005890, -0.0001855),  # lat.incis ← typo gecorrigeerd
    3: (16.5369, 1.6010, -0.2494, 0.01087, 0.00021, -0.0000182),    # cuspidaat
    4: (21.8618, -2.3031, 0.5330, -0.04075, 0.00062, 0.0000199),    # 1e premol
    5: (39.2681, -7.3113, 1.2340, -0.12192, 0.00626, -0.0001260),   # 2e premol
    6: (16.8835, -0.5688, 1.5433, -0.06519, -0.01454, 0.0009019),   # 1e molaar
    7: (25.4265, 4.6241, -3.0787, 0.95774, -0.10923, 0.0040876),    # 2e molaar
}
PESA_COEF_MAND = {
    1: (21.4600, -6.6888, 2.4638, -0.39094, 0.02743, -0.0007116),
    2: (16.4395, -1.0337, 0.4146, -0.05711, 0.00257, -0.0000211),
    3: (24.6992, -3.5868, 0.6903, -0.05799, 0.00189, -0.0000142),
    4: (24.6866, -4.8531, 1.3992, -0.18028, 0.01037, -0.0002229),
    5: (13.1705, 5.0958, -1.0989, 0.10864, -0.00559, 0.0001179),
    6: (19.1229, -12.2566, 5.5750, -0.78145, 0.04566, -0.0009711),
    7: (46.6148, -43.1558, 16.7577, -2.48858, 0.16174, -0.0038873),
}
# Totaal worteloppervlak per tandtype (mm²), Jepsen 1963.
ROOT_TOTAL_MAX  = {1: 204, 2: 179, 3: 273, 4: 234, 5: 220, 6: 433, 7: 431}
ROOT_TOTAL_MAND = {1: 154, 2: 168, 3: 268, 4: 180, 5: 207, 6: 431, 7: 426}


def _coef_for(fdi: int):
    typ = fdi % 10
    if typ == 8:
        typ = 7
    table = PESA_COEF_MAX if (fdi // 10) in (1, 2) else PESA_COEF_MAND
    return table.get(typ)


def root_total(fdi: int) -> float:
    typ = fdi % 10
    if typ == 8:
        typ = 7
    table = ROOT_TOTAL_MAX if (fdi // 10) in (1, 2) else ROOT_TOTAL_MAND
    return float(table.get(typ, 0.0))


def poly(fdi: int, x: float) -> float:
    """Nesse-polynoom voor het tandtype van `fdi`, geëvalueerd op `x` mm
    (gem. pocketdiepte voor PESA; gem. aanhechtingsniveau voor ALSA).
    Resultaat in mm². Wordt geclampt op ≥ 0 en op ≤ Totaal (anatomische
    grens uit Jepsen 1963)."""
    coef = _coef_for(fdi)
    if not coef or x is None or x <= 0:
        return 0.0
    raw = sum(c * x ** (i + 1) for i, c in enumerate(coef))
    return max(0.0, min(raw, root_total(fdi)))


if __name__ == "__main__":
    # Quick demo: tand 12 bij CAL = 2 mm reproduceert Nesse 2008 Fig 2a (34.04 mm²).
    print(f"FDI 12 @ CAL=2.0 mm  → ALSA = {poly(12, 2.0):.2f} mm²  (Nesse Fig 2a: 34.04)")
    print(f"FDI 12 @ CAL=3.33 mm → ALSA = {poly(12, 3.33):.2f} mm²  (Nesse Fig 2c: 56.11)")
