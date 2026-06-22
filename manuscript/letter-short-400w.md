# Letter to the Editor — STRIKTE 400-WOORD VERSIE

*Voor de Letter to the Editor categorie van J Clin Periodontol.
Strikt 400 woorden tekst + max 5 refs + 1 figuur. Geen tabellen.*

---

**Title:** A decimal-shift typographical error in Table 1 of Nesse et al.
(2008): the maxillary lateral incisor *a*₅ coefficient

**Authors:** T.H. van den Berg¹ *[+ max 2 co-authors]*
¹ Practice for Periodontology Haarlem, The Netherlands

**Correspondence:** T.H. van den Berg, *[email] · ORCID*

**Conflict of interest:** None declared.

---

Dear Editor,

The PISA framework by Nesse et al. (2008) uses a per-tooth-type 6th-degree
polynomial to convert probing measurements to root-surface areas.
Implementing this framework clinically, we observed that for one specific
tooth — the maxillary lateral incisor (FDI 12/22) — the polynomial
overshoots the anatomical total root surface (Jepsen, 1963) at attachment
levels as low as ≈4.6 mm. After clamping, this forces remaining
attachment surface (RAS = Total − ALSA) to zero in any patient with
moderate periodontitis, which is clinically implausible. No other tooth
type shows this behaviour within the clinical range (1–8 mm).

Inspection of Table 1 in the original paper revealed that the *a*₅
coefficient for the maxillary lateral incisor (0.05890) is one order of
magnitude larger than for either centrally adjacent anterior tooth
(central incisor 0.01126; canine 0.00021). The positive *a*₅ term drives
explosive x⁵ growth, explaining the saturation at moderate AN.

To distinguish a transcription artefact from a typographical error in
the printed table, we cross-validated against the worked example
spreadsheets the original paper itself provides (Figure 2a–c). In Figure
2a, tooth 12 at mean CAL=2 mm shows ALSA = 34.04 mm². Evaluating the
polynomial with the printed *a*₅ (0.05890) gives 35.74 mm² — off by 5%.
Evaluating with *a*₅ shifted one decimal place (0.005890) gives 34.05
mm² — matching 34.04 within 0.03%. The corrected coefficient was further
validated against Patient 3 tooth 12 (ALSA = 56.11, back-solved
CAL = 3.33), and systematically across all 14 tooth types and 25 anchored
reference points from Figure 2a–c, reproducing every value within ≤ 0.17
mm² (< 0.1 %). The supplementary spreadsheet at parsprototo.info
implicitly encodes the corrected value.

We therefore identify the printed 0.05890 as a decimal-shift typographical
error and recommend the Editorial Office consider a corrigendum: Table 1,
maxillary lateral incisor, *a*₅ should read **0.005890**.

A reproducibility suite (MIT-licensed) and the verification figure are
available at *[Zenodo DOI placeholder]*.

*[~340 words; ruimte voor lichte aanpassing]*

---

**Figure 1.** Polynomial output (ALSA, mm²) versus AN (mm) for the
maxillary lateral incisor. Dashed: printed *a*₅; solid: corrected *a*₅;
dotted: anatomical total root surface (Jepsen 1963).

---

**References (max 5):**

1. Nesse W, Abbas F, van der Ploeg I, Spijkervet FKL, Dijkstra PU, Vissink A.
   Periodontal inflamed surface area: quantifying inflammatory burden.
   *J Clin Periodontol* 2008;35:668–673. doi:10.1111/j.1600-051X.2008.01249.x

2. Jepsen A. The measurement of clinical attachment level in dental research.
   *Acta Odontol Scand* 1963;21:35–41.

3. Hujoel PP, White BA, García RI, Listgarten MA. The dentogingival epithelial
   surface area revisited. *J Periodontal Res* 2001;36:48–55.
   doi:10.1034/j.1600-0765.2001.00011.x

4. parsprototo.info. PISA spreadsheet [Internet]. Available at:
   https://parsprototo.info/ (accessed 22 June 2026).

5. van den Berg TH. Perioscope — verification suite for the Nesse 2008 PISA
   polynomial coefficients. *Zenodo* 2026; doi:10.5281/zenodo.NNNNNNNN

---

## Notitie voor schrijver

- Word-count is gecheckt: ~340 woorden in de letter-body, ruimte voor
  fine-tuning.
- Geen subkopjes mogen — alles is één lopende paragrafenstroom.
- Eén figuur is veilig binnen de 5-ref/3-auteur regel; geen tabellen.
- Volledig bewijs zit in:
  (i) de zin "match within 0.03 %"
  (ii) de verwijzing naar systematische validatie 14 tandtypen, 25 punten
  (iii) Figuur 1
  Dat is voldoende voor de Editor om door te zetten naar de Nesse-team
  voor formele corrigenda-verificatie.
