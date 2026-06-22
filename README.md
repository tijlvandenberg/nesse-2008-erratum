# Erratum supporting materials — Nesse et al. (2008) PISA framework

Materialen behorende bij een **Letter to the Editor / Corrigendum** bij
*Journal of Clinical Periodontology*, over een decimaal-typo in
Tabel 1 van het artikel:

> Nesse W, Abbas F, van der Ploeg I, Spijkervet FKL, Dijkstra PU, Vissink A.
> *Periodontal inflamed surface area: quantifying inflammatory burden*.
> J Clin Periodontol 2008;35:668–673. doi:10.1111/j.1600-051X.2008.01249.x

## De bevinding in één regel

In Tabel 1 staat voor de bovenste laterale incisief (FDI 12/22) als a₅
de waarde **0.05890**. Op basis van de voorbeeldspreadsheets in
Figuur 2a–c van datzelfde artikel lijkt het werkelijke (door de auteurs
gebruikte) getal **0.005890** te zijn — één decimaalplek verschoven.
Met die correctie reproduceer ik alle 25 anker-ALSA-waarden uit de drie
voorbeeldpatiënten binnen 0.17 mm² (< 0.1 %).

## Inhoud

| Map | Inhoud |
|---|---|
| `manuscript/` | Engelse Letter to the Editor (volledig + 400-woord variant), cover letter en LaTeX-source |
| `figure/` | Figuur 1 (PDF + PNG) met matplotlib-source |
| `correspondence/` | Nederlandse mail aan Dr. Nesse (cc Abbas, Vissink) + Engelse pre-notification aan JCPE Editorial Office |
| `verification/` | Stand-alone Python-implementatie + pytest-regressie-suite die alle 25 ankerpunten reproduceert |

## Status

Op dit moment (juni 2026):

1. Eerst contact met Dr. Nesse en oorspronkelijke co-auteurs — uitnodiging tot een corrigendum onder hun eigen auteurschap.
2. Parallelle pre-notification aan JCPE Editorial Office.
3. Pas indien geen reactie binnen ~4 weken: formele inzending Letter to the Editor.

**Voorkeur**: correctie verschijnt onder de oorspronkelijke auteurs,
zonder mijn auteurschap. Mijn motivatie is uitsluitend dat de fout uit
de literatuur verdwijnt voordat hij verder propageert in software en
cohortstudies.

## Reproductie

```bash
cd verification
python3 nesse_polynomial.py            # snelle demo
python3 -m pytest test_nesse_coef.py   # volledige regressie-test
```

## Licentie

- Code (`verification/`, `figure/fig1-source.py`): **MIT** (zie LICENSE).
- Tekst en figuren in `manuscript/`, `correspondence/`, `figure/`:
  **CC BY 4.0** (zie LICENSE-DOCS).

Vrij te citeren, te hergebruiken en te verbeteren — graag zelfs.
