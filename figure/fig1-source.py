"""Figuur 1 voor de erratum-letter (J Clin Periodontol).

Toont de polynoom-uitkomst voor de bovenste laterale incisief
als functie van AN, voor zowel de printed (typo) als de
corrected coëfficiënt, met de Jepsen-totaal als horizontale referentie.

Uitvoer: docs/nesse-erratum/nesse-erratum-fig1.{pdf,png} (1-kolom A4-ready).
Gebruikt enkel numpy + matplotlib.

Layout-keuzes:
- Wijder canvas (5.4 × 4.0 inch) zodat labels ademruimte hebben.
- Legenda linksboven, compact, in een eigen box.
- Annotaties strikt buiten de curves geplaatst en met arrow-callouts
  zodat overlap met de legenda of de gestreepte-rode curve uitgesloten is.
- Linewidth en kleur-saturatie iets verhoogd voor zwart-wit-print-leesbaarheid.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

# Coëfficiënten max #2 (laterale incisief boven)
TYPO = (18.7571, -1.6471, 0.5258, -0.07900, 0.05890, -0.0001855)
CORR = (18.7571, -1.6471, 0.5258, -0.07900, 0.005890, -0.0001855)
TOTAL = 179.0          # Jepsen 1963 (Acta Odontol Scand 21:35)

COL_TYPO = '#b91c1c'   # rood
COL_CORR = '#1e3a8a'   # diep blauw
COL_TOTAL = '#475569'  # neutraal grijs

def poly(coef, x):
    return sum(c * x ** (i + 1) for i, c in enumerate(coef))

x = np.linspace(0, 8, 600)
y_typo = np.array([poly(TYPO, xi) for xi in x])
y_corr = np.array([poly(CORR, xi) for xi in x])

Y_MAX = 295
y_typo_plot = np.minimum(y_typo, Y_MAX - 5)

fig, ax = plt.subplots(figsize=(5.4, 4.0), dpi=150)

ax.plot(x, y_typo_plot, ls='--', lw=1.8, color=COL_TYPO,
        label="As printed (a$_5$ = 0.05890)", zorder=3)
ax.plot(x, y_corr, ls='-', lw=2.0, color=COL_CORR,
        label="Corrected (a$_5$ = 0.005890)", zorder=4)

ax.axhline(TOTAL, color=COL_TOTAL, lw=1.0, ls=':',
           label=f"Total root surface (Jepsen 1963) = {TOTAL:.0f} mm$^2$",
           zorder=2)

ax.fill_between(x, TOTAL, y_typo_plot, where=(y_typo_plot > TOTAL),
                color=COL_TYPO, alpha=0.08, zorder=1,
                label="Overshoot region (printed coefficient)")

SAT_X = 4.54
ax.plot(SAT_X, TOTAL, marker='s', ms=7, mfc=COL_TYPO, mec=COL_TYPO, zorder=5)
ax.annotate(
    f"Saturation\nat AN $\\approx$ {SAT_X} mm",
    xy=(SAT_X, TOTAL),
    xytext=(6.6, 245),
    fontsize=8.5, color=COL_TYPO,
    ha='center',
    bbox=dict(boxstyle='round,pad=0.35', fc='white',
              ec=COL_TYPO, lw=0.6, alpha=0.95),
    arrowprops=dict(arrowstyle='->', color=COL_TYPO, lw=0.8,
                    connectionstyle='arc3,rad=-0.15')
)

for an in (4, 5):
    val = poly(CORR, an)
    ax.plot(an, val, marker='o', ms=5, mfc=COL_CORR, mec=COL_CORR, zorder=5)

ax.annotate(
    "AN = 4 mm\nALSA $\\approx$ 67 mm$^2$",
    xy=(4, poly(CORR, 4)),
    xytext=(1.8, 105),
    fontsize=8.5, color=COL_CORR,
    ha='center',
    bbox=dict(boxstyle='round,pad=0.30', fc='white',
              ec=COL_CORR, lw=0.6, alpha=0.95),
    arrowprops=dict(arrowstyle='->', color=COL_CORR, lw=0.8,
                    connectionstyle='arc3,rad=0.15')
)

ax.annotate(
    "AN = 5 mm\nALSA $\\approx$ 85 mm$^2$",
    xy=(5, poly(CORR, 5)),
    xytext=(6.9, 55),
    fontsize=8.5, color=COL_CORR,
    ha='center',
    bbox=dict(boxstyle='round,pad=0.30', fc='white',
              ec=COL_CORR, lw=0.6, alpha=0.95),
    arrowprops=dict(arrowstyle='->', color=COL_CORR, lw=0.8,
                    connectionstyle='arc3,rad=-0.15')
)

ax.set_xlabel("Mean attachment level AN (mm)", fontsize=10)
ax.set_ylabel("ALSA (mm$^2$)", fontsize=10)
ax.set_xlim(0, 8)
ax.set_ylim(0, Y_MAX)
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])
ax.set_yticks([0, 50, 100, 150, 179, 200, 250])
ax.tick_params(axis='both', labelsize=9)
ax.grid(True, ls=':', lw=0.5, alpha=0.4)

for lbl in ax.get_yticklabels():
    if lbl.get_text() == '179':
        lbl.set_color(COL_TOTAL)
        lbl.set_fontweight('bold')

ax.set_title("Maxillary lateral incisor: Nesse 2008 polynomial output",
             fontsize=10.5, pad=8)

legend = ax.legend(
    loc='upper left', bbox_to_anchor=(0.02, 0.98),
    fontsize=7.8, frameon=True, framealpha=0.95,
    edgecolor='#cbd5e1', borderpad=0.6, labelspacing=0.35
)
legend.get_frame().set_linewidth(0.5)

plt.tight_layout()
plt.savefig("nesse-erratum-fig1.pdf", bbox_inches='tight')
plt.savefig("nesse-erratum-fig1.png", bbox_inches='tight', dpi=300)
print("✓ Figuur opgeslagen: nesse-erratum-fig1.{pdf,png}")
