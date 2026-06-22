# E-mail aan Dr. W. Nesse (NL) — t.b.v. Letter to the Editor over typo Nesse 2008

*Klaar om te kopiëren naar je e-mail-client. Pas e-mailadressen, ORCID
en eventueel je telefoonnummer aan. Engelse cover-letter, manuscript en
overige documenten blijven in het Engels.*

---

**Aan:** `kaakchirurgie@wza.nl` (t.a.v. Dr. W. Nesse — graag doorgeleiden)
**CC:** `f.abbas@umcg.nl`; `a.vissink@umcg.nl`
**Onderwerp:** Mogelijke decimaal-typo in Nesse et al. (2008) Tabel 1 — uitnodiging tot co-auteurschap erratum

---

Beste Dr. Nesse,
*(en in cc: Prof. Abbas en Prof. Vissink)*

Met enige aarzeling stuur ik u deze mail. Tijdens het ontwikkelen van
een eigen parodontologie-applicatie (Perioscope, voor onze praktijk in
Haarlem) ben ik bij implementatie van uw PISA-framework op iets gestuit
dat er met grote waarschijnlijkheid uitziet als een drukfout in Tabel 1
van uw 2008-paper in *J Clin Periodontol*. Het gaat om één coëfficiënt
in één tand-rij — verder is alles in de tabel verbluffend nauwkeurig en
reproduceer ik uw drie voorbeeldspreadsheets uit Figuur 2a–c probleemloos
binnen 0.1 %.

Vervelend dat juist ik degene blijk die u hierop wijst — als collega
parodontoloog, en Nederlander, voel ik me er ongemakkelijk bij om het
overgrote werk dat u en de co-auteurs in deze paper hebben gestoken op
één punt te bekritiseren. Maar het probleem is klinisch wel merkbaar:
voor de boven-laterale incisief klapt de ALSA-berekening bij AN ≈ 4.6 mm
al tegen het Jepsen-totaal aan, met RAS = 0 als gevolg — terwijl er
klinisch nog ruim aanhechting overblijft. Bij implementatie in de
software vielen mij steeds dit soort onmogelijke RAS-waarden op,
specifiek bij tand 12 en 22.

Concreet:

- **Probleem.** In Tabel 1 staat voor de bovenste laterale incisief
  (FDI 12/22) als a₅ de waarde **0.05890**.
- **Hypothese.** Op basis van uw eigen voorbeeldspreadsheets in Figuur 2a–c
  lijkt de werkelijk gebruikte waarde **0.005890** te zijn — één
  decimaalplek verschoven.
- **Verificatie.** Bij CAL = 2 mm geeft Patiënt 1 in Figuur 2a voor
  tand 12 ALSA = 34.04 mm². De gedrukte coëfficiënt levert 35.74
  (5 % afwijking); de gecorrigeerde levert 34.05 — exact gelijk binnen
  0.03 %. Voor Patiënt 3 tand 12 (ALSA = 56.11) reproduceer ik bij
  CAL = 3.33 mm precies 56.06 — wederom binnen 0.1 %. Systematische
  cross-check op alle 14 tandtypen en 25 ankerpunten uit de drie
  voorbeeldpatiënten valt overal binnen **0.17 mm²** (< 0.1 %).
- **Conclusie.** De spreadsheets die u online deelt op parsprototo.info
  gebruiken impliciet 0.005890; de afwijking lijkt uitsluitend in de
  gedrukte tabel te zitten.

Ik heb het uitgewerkt tot een Letter to the Editor / Brief Communication
voor *J Clin Periodontol*, inclusief figuur, twee tabellen, en een
reproductie-test-suite (open-source, MIT-licentie). Alle materialen
staan klaar in:

- Concept-manuscript, cover letter, figuur en verificatie-code (publiek leesbaar zonder GitHub-login): https://github.com/tijlvandenberg/nesse-2008-erratum
- Origineel artikel ter referentie: doi:10.1111/j.1600-051X.2008.01249.x

**Mijn vraag.** Wat is uw voorkeur voor het vervolg?

1. *Erratum onder uw eigen team*. Wat mij betreft de mooiste route: u en
   uw 2008-co-auteurs dienen zelf een formele corrigendum-mededeling in
   bij het tijdschrift, op basis van mijn observaties. Ik lever het
   bewijs, de code en de figuren aan, zonder eigen co-auteurschap te
   willen. Mijn motivatie is dat de fout uit de literatuur verdwijnt
   voordat een nieuwe softwareleverancier of cohortstudie 'm onbewust
   overneemt — niet om er zelf publication-credit voor te krijgen.

2. *Gezamenlijk co-auteurschap*. Mocht u dat verkiezen, dan dien ik
   graag samen met u (en wie van de oorspronkelijke co-auteurs wil
   meeschrijven) de Letter in. De redactionele eindversie en submission
   kan ik voor mijn rekening nemen.

3. *Solo*. Als u liever niet betrokken wilt zijn, dien ik de Letter
   solo in, met expliciete vermelding van uw team's voorbeeldd
   spreadsheets als referentie en met dankzegging voor de transparantie
   waarmee u die destijds beschikbaar heeft gemaakt — zonder die had ik
   de typo nooit kunnen pinpointen.

Mijn voorkeur is route 1 of 2; route 3 alleen als reserve.

Ik realiseer me dat u nu MKA-chirurg bent in Assen en niet meer dagelijks
met PISA werkt. Dat is ook geen probleem — mocht u liever willen dat
Prof. Abbas of Prof. Vissink het verder oppakt (zij staan immers nog
volop in het parodontologie/orale geneeskunde-onderzoek), dan kunnen we
dat ook zo doen. Vandaar de cc.

Eerlijk vermeld: ik heb deze fout vandaag al in onze eigen software
gecorrigeerd, met de klinische gevolgen die u zou verwachten — RAS bij
matig gevorderde parodontitis op tand 12/22 ligt nu rond 50–95 mm² in
plaats van 0. Voor onze eigen praktijk is de zaak dus klinisch al
afgehandeld; wat resteert is louter de wetenschappelijke
literatuur-correctie.

Reactietijd: neem gerust een paar weken. Bij geen reactie binnen ~4
weken neem ik vrijblijvend nog eens kort contact op.

Met vriendelijke groet,

T.H. (Tijl) van den Berg
Parodontoloog NVvP
Praktijk voor Parodontologie Haarlem
*[adres, telefoon, e-mail, ORCID]*

---

**Bijlagen** (PDF's, op verzoek per mail of via de GitHub-link):

1. Concept-Letter (English): `nesse-2008-erratum-letter.docx`
2. Concept-Letter strikt 400 wd (English): `nesse-2008-erratum-letter-short.docx`
3. Cover letter (English): `nesse-erratum-cover-letter.docx`
4. Figuur 1 (PDF): `nesse-erratum-fig1.pdf`
5. Reproductie-test-suite + stand-alone Python-implementatie:
   `verification/` in https://github.com/tijlvandenberg/nesse-2008-erratum
