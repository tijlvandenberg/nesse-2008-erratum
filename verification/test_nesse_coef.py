"""Regressie-test voor de Nesse 2008 polynoom-coëfficiënten in paro_codec.

Achtergrond: de gedrukte Tabel 1 in Nesse W et al. (2008) "Periodontal inflamed
surface area" (J Clin Periodontol 35:668-673, doi:10.1111/j.1600-051X.2008.01249.x)
bevat minstens één typo (max #2 / laterale incisief, a₅: 0.05890 → moet zijn
0.005890). De ECHT-juiste coëfficiënten staan in de bijgeleverde voorbeeld-
spreadsheets (Fig 2a-c in dezelfde paper), die ALSA-uitkomsten tonen voor drie
fictieve patiënten.

Deze test laadt elke ALSA-referentiewaarde uit Fig 2a/b/c en checkt dat onze
polynoom een CAL kan vinden die exact dat ALSA reproduceert (binnen 2 %).
Faalt deze test, dan is iemand per ongeluk een coëfficiënt aan het aanpassen
zonder de Nesse-validatie te checken — of de gepubliceerde Tabel 1 bevat
nóg een typo die we hier moeten documenteren.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from perioscope.paro_codec import _PESA_COEF_MAX, _PESA_COEF_MAND, _poly


# Vaste anker-punten: (FDI, gemiddelde CAL, verwachte ALSA). Voor elk tandtype
# uit Nesse Fig 2a-c kennen we minstens één combinatie waarbij de polynoom-
# uitkomst EXACT de getoonde ALSA reproduceert (gevonden door 0.005-mm scan).
# Door de CAL hier hard te fixen kan de test geen alternatieve x-waarde meer
# vinden om een coëfficiënt-fout op te vangen — een typo zou poly(cal) doen
# afwijken van de verwachte ALSA en de test direct laten falen.
# Bron-PDF: https://parsprototo.info/docs/PISA%20quantifying%20inflammatory%20burden.pdf
NESSE_REF = [
    # FDI, CAL (mm), verwachte ALSA (mm²), patient-label voor foutmelding
    # — bovenkaak Patient 1
    (11, 2.00,  28.72, "Pt1"),
    (12, 2.00,  34.04, "Pt1"),   # ← key: vangt de a₅-typo (zou 35.74 geven)
    (13, 2.50,  47.89, "Pt1"),
    (14, 2.00,  38.14, "Pt1"),
    (15, 2.67,  70.76, "Pt1"),
    (16, 2.50,  59.02, "Pt1"),
    (17, 2.67,  77.48, "Pt1"),
    (24, 2.00,  38.14, "Pt1"),
    (25, 2.00,  57.40, "Pt1"),
    # — bovenkaak Patient 2 (severe local)
    (16, 3.50, 102.53, "Pt2"),
    (17, 3.33, 101.00, "Pt2"),
    # — bovenkaak Patient 3 (severe generalized)
    (11, 5.33,  95.77, "Pt3"),
    (12, 3.33,  56.11, "Pt3"),   # ← extra a₅-check op hogere CAL
    (16, 8.17, 389.94, "Pt3"),
    (17, 7.33, 309.97, "Pt3"),
    # — onderkaak Patient 1
    (31, 2.00,  30.45, "Pt1"),
    (34, 2.33,  44.29, "Pt1"),
    (35, 2.33,  47.37, "Pt1"),
    (36, 2.33,  28.55, "Pt1"),
    (37, 2.50,  26.29, "Pt1"),
    # — onderkaak Patient 2 (severe local in laatste molaren)
    (36, 8.33, 275.66, "Pt2"),
    (37, 8.00, 278.57, "Pt2"),
    (47, 4.50, 108.62, "Pt2"),
    # — onderkaak Patient 3 (severe generalized)
    (31, 4.00,  61.60, "Pt3"),
    (37, 7.50, 264.07, "Pt3"),
]


def _coef_for(fdi):
    """Coëfficiënten voor het tandtype van een FDI (8 → 7e regel)."""
    typ = fdi % 10
    if typ == 8:
        typ = 7
    table = _PESA_COEF_MAX if (fdi // 10) in (1, 2) else _PESA_COEF_MAND
    return table.get(typ)


def test_alle_tandtypes_reproduceren_nesse_spreadsheet():
    """Voor elke vaste (FDI, CAL) in NESSE_REF: polynoom moet binnen 0.5 mm²
    (of 1 % van target, schaalt voor grote waarden) Nesse's spreadsheet
    reproduceren.

    Faalt deze test? Mogelijke oorzaken:
    1. Coëfficiënt-tabel `_PESA_COEF_MAX` of `_PESA_COEF_MAND` is per ongeluk
       gewijzigd (controleer git blame op paro_codec.py).
    2. De gedrukte Tabel 1 bevat nóg een typo die we moeten documenteren —
       update deze test met de gevonden waarde en bewijsvoering.
    """
    falen = []
    for fdi, cal, expected, pt in NESSE_REF:
        coef = _coef_for(fdi)
        actual = _poly(coef, cal)
        # tolerantie: 0.5 mm² of 1 % van verwachte (welke groter is).
        tol = max(0.5, expected * 0.01)
        if abs(actual - expected) > tol:
            falen.append((fdi, pt, cal, expected, actual))

    if falen:
        regels = [
            f"  FDI {f} ({p}, CAL={c}): verwacht ALSA={e:.2f}, "
            f"polynoom gaf {a:.2f} (Δ {a-e:+.2f} mm²)"
            for f, p, c, e, a in falen
        ]
        msg = "\n".join(regels)
        raise AssertionError(
            f"\n{len(falen)} referentiewaarde(n) reproduceren NIET binnen 1 % / 0.5 mm²:\n{msg}"
        )


def test_max_lat_incis_typo_blijft_gefixt():
    """Specifiek voor de bekende typo: a₅ voor max lateral incisor moet
    0.005890 zijn (niet 0.05890 zoals in de gedrukte Tabel 1).

    Toets: poly(2.0 mm) voor tandtype 2 max moet ~34.04 mm² geven (matcht Pt1
    Fig 2a, tand 12, CAL gem. = 2 mm). Met de typo-versie zou de uitkomst
    35.74 mm² zijn — die afwijking pakken we hier expliciet."""
    coef = _PESA_COEF_MAX[2]
    val = _poly(coef, 2.0)
    assert 33.5 < val < 34.5, (
        f"Max lat.incis poly(2) = {val:.2f}, verwacht ~34.04 "
        f"(Nesse Fig 2a tand 12). Mogelijk a₅-typo herintroduceerd: "
        f"check of paro_codec.py regel 197 nog 0.005890 heeft."
    )
