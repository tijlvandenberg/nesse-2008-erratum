# Cover letter — Letter to the Editor submission

**To:** Prof. Nikolaos Donos, Editor-in-Chief, *Journal of Clinical Periodontology*
*(verifieer aanhef + officiële Editor-titel vóór verzending — Prof. Donos in functie sinds 1 april 2026)*
**Re:** Letter to the Editor — "Identification of a decimal-shift typographical error in Table 1 of Nesse et al. (2008): the a₅ coefficient for the maxillary lateral incisor"

---

*[Practice for Periodontology Haarlem, address]*
*[date]*

Dear Professor Donos,

We submit the enclosed Letter to the Editor for your consideration. The
letter is, in essence, a quiet correction note: it identifies a single
decimal-shift typographical error in Table 1 of Nesse, Abbas, van der
Ploeg, Spijkervet, Dijkstra and Vissink (2008), "Periodontal inflamed
surface area: quantifying inflammatory burden" (*J Clin Periodontol*
35:668–673). Specifically, the a₅ coefficient for the maxillary lateral
incisor is printed as 0.05890 and should read 0.005890. We write with
appreciation for the original authors' contribution — the PISA framework
has shaped the field — and have first contacted Dr. Nesse and his
co-authors with the same evidence, inviting them to consider issuing a
Corrigendum under their own authorship.

**Our strong preference is for the correction to appear under the
original authors' names alone, without us as co-authors.** Our
motivation is service to the field, not authorship credit. Should
Dr. Nesse and colleagues choose to submit a Corrigendum within a
reasonable interval (we suggested ~4 weeks from our 22 June 2026
communication), we would respectfully withdraw the enclosed Letter and
remain available to provide the underlying data, code and figures as
supporting material. The enclosed Letter is therefore intended only as
a fallback should the original authors decline or not respond.

The error was identified during clinical implementation of the PISA framework, where we observed implausible saturation of ALSA (attachment-loss surface area) at moderate clinical attachment levels for lateral incisors only. We then verified the correction directly against the example spreadsheets that the original authors helpfully published alongside the paper (Figure 2a–c). The printed coefficient gives PESA = 35.74 mm² for tooth 12 at CAL = 2 mm; the corrected coefficient gives 34.05 mm², matching the spreadsheet value of 34.04 mm² to within 0.03 %. A systematic cross-validation across all 14 tooth types and three example patients (25 anchored reference points) reproduces every published value within ≤ 0.17 mm² (< 0.1 %).

The error is **clinically consequential**: in periodontitis stage II or above, the maxillary lateral incisor is routinely measured with attachment loss ≥ 5 mm, at which the printed polynomial saturates to total root surface and forces remaining attachment to zero. Cohort studies and clinical software that rely on the printed coefficient systematically over-estimate ALSA and under-estimate remaining attachment for these teeth.

We propose this letter as an erratum-equivalent communication, with the practical aim of ensuring future researchers and software developers use the correct value. The official PISA spreadsheet at parsprototo.info already encodes the corrected value, which provided our gold-standard reference.

A reproducibility test suite (Python, MIT-licensed) that re-evaluates every entry in Table 2 of the letter is openly available — no login required — at <https://github.com/tijlvandenberg/nesse-2008-erratum> (manuscript drafts, figure with source, correspondence and verification code). A Zenodo DOI for the same materials will be added prior to formal acceptance.

**Originality:** This letter has not been submitted to any other journal and has no prior or partial publication.

**Conflicts of interest:** None declared. None of the authors are affiliated with the original Nesse et al. (2008) team or with parsprototo.info.

**Author contributions:** [in te vullen]

We thank you for considering this letter. We believe its publication will reduce the propagation of this error in periodontal-burden quantification and serve as an example of the practical value of authors publishing their working spreadsheets — without which this discrepancy could not have been resolved unambiguously.

Yours sincerely,

T.H. van den Berg,
*Corresponding author* — [email], [ORCID]
On behalf of the co-authors

---

**Enclosures:**

1. Main letter (manuscript)
2. Figure 1 (PDF + PNG, 1-column)
3. Tables 1–2 (in-line in manuscript)
4. Supplementary material: reproducibility test suite (`tests/test_nesse_coef.py`) and verification figure script (`docs/nesse-erratum-figure.py`)

**Suggested reviewers** (no conflict of interest, expertise in PISA/quantitative periodontology):
- *[2–3 namen in te vullen door eerste auteur — vermijd Nesse-co-auteurs en parsprototo-affiliaten]*
