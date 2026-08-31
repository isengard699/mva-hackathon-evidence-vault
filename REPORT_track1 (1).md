# Track 1 — Methods Report

**MVA Hackathon 2026 · Proband: PROBAND01** **Participant:** Saruman-314 **Model:** `bub1b-comphet-vep-targeted` **Date:** 2026-08-28

---

## 1\. Summary

A targeted, hypothesis-driven analysis of the proband's whole-genome VCF identified **two heterozygous variants in *BUB1B*** as the primary candidate, proposed as a **compound heterozygous pair**:

|  | Consequence | Protein | Population AF | Filter |
| :---- | :---- | :---- | :---- | :---- |
| Allele 1 | `stop_gained` | p.Leu737Ter | 1.0 × 10⁻⁴ | PASS |
| Allele 2 | `missense_variant` | p.Asn1002Lys | absent | PASS |

Out of **265** non-reference variants across five spindle-assembly-checkpoint genes, these were the **only two** meeting both criteria of the prioritisation rule (damaging consequence class *and* population frequency \< 1%).

**The phase of these two variants is inferred, not demonstrated.** See §5.

---

## 2\. Rationale for a targeted approach

*Mosaic Variegated Aneuploidy* is associated with biallelic aberrations in **BUBR1 (*BUB1B*), *CEP57* and *TRIP13*** (Sieben et al., *J Clin Invest* 2020, DOI:10.1172/JCI126863). *BUB1* and *BUB3* were added as members of the same spindle-assembly checkpoint, and appear alongside the three canonical genes in curated MVA gene sets.

The proband's reported phenotype — rhabdomyosarcoma, nephrocalcinosis, growth restriction, adverse perinatal history and parental recurrent pregnancy loss (challenge phenotype document) — is consistent with a chromosomal-instability disorder. The challenge documentation explicitly notes that significance lies in the **co-occurrence** of these features rather than in any single finding, and that parental reproductive loss should be treated as phenotypic signal.

A five-gene targeted analysis was therefore chosen over a genome-wide scan: it is faster, fully auditable, and its failure mode is explicit (if nothing is found in these genes, the hypothesis is refuted and the search widens).

---

## 3\. Methods

All steps are reproducible with the Python standard library. No `bcftools`, no alignment, no local reference genome required.

### 3.1 Data

Only `WGS_EX2312012_HGWCNDSX7.vcf.gz` (315 MB) and its index were downloaded. The \~84.7 GB of FASTQ files were **not** used: no re-alignment was performed, so the variant calls are those provided by the organisers (GATK `VariantFiltration`).

Assembly was determined from contig lengths in the VCF header (`chr1 = 248,956,422` → **GRCh38**), because the `##reference` field is uninformative (`file://refGenome/genome.fasta`). Contigs are named without a `chr` prefix.

### 3.2 Region extraction

Gene coordinates were **queried from the Ensembl REST API at runtime** and printed before use — no coordinates are hard-coded. The script aborts if Ensembl returns an assembly other than GRCh38.

Regions: *BUB1B*, *CEP57*, *TRIP13*, *BUB1*, *BUB3*, each padded **± 10 kb** to capture splice-region and proximal regulatory variants.

Genotypes `0/0`, `./.` and no-calls were discarded. **265 variants** retained.

### 3.3 Annotation

Ensembl VEP REST API: consequence terms, canonical transcript, HGVS, exon/intron number, population frequencies, SIFT and PolyPhen.

Three variants could not be annotated (one multiallelic, two rejected by the API). They are recorded as `REVISAR` — **declared unevaluated, not discarded**. A technical failure that disappears from view is how a real finding gets lost.

### 3.4 Prioritisation

- **HIGH** — consequence in the damaging classes (through `protein_altering_variant`) **and** population AF \< 1% or absent  
- **medium** — rare, lower-impact consequence  
- **low** — AF ≥ 1%

**255 of 265 variants were excluded on frequency alone.** A variant carried by an appreciable fraction of the population cannot cause a disorder affecting fewer than 50 individuals worldwide.

---

## 4\. ACMG/AMP criteria — proposed, not assigned

| Variant | Criteria | Status |
| :---- | :---- | :---- |
| p.Leu737Ter | PVS1, PM2, PM3 | **Proposed** |
| p.Asn1002Lys | PM2, PM3, PP3 | **Proposed** |

These are **candidate criteria, not a classification**. Formal ACMG/AMP application requires expert review and gene-specific VCEP specifications where they exist.

- **PVS1** requires confirming that loss of function is the disease mechanism for *BUB1B* and that the transcript is subject to nonsense-mediated decay. Not verified here.  
- **PM3** requires *trans* configuration. **Not demonstrable — see below.**  
- **PP3** should only be claimed if in-silico predictors concur.

---

## 5\. Limitations

Stated explicitly, because they change how this result should be read.

### 5.1 Phase is inferred, not demonstrated

**The VCF contains a single sample.** There is no parental data. That the two variants lie on opposite alleles is an inference from the recessive inheritance described for MVA and from phenotypic coherence — **not an observation**.

This is not a technicality. It is the difference between a proposed compound heterozygote and a confirmed one, and it constrains ACMG **PM3** for both variants. Any downstream mechanistic or therapeutic reasoning inherits this uncertainty.

### 5.2 The missense allele is not established as pathogenic

Absence from population databases is suggestive, not sufficient. Without functional data or an established ClinVar classification, **p.Asn1002Lys remains a VUS**. The truncating allele stands on its own; this one does not.

### 5.3 Three variants remain unevaluated

Three *BUB3* variants could not be annotated. They are reported in the submission with low EPCR values and flagged. They are **not excluded**.

### 5.4 Variant calling was not re-done

Analysis depends entirely on the provided call set. Variants missed by the original pipeline — structural variants, deep-intronic events, calls lost to filtering — would not be recovered here.

---

## 6\. Confidence calibration

The primary candidate was assigned **EPCR \= 0.95**, not 1.0.

The reasoning: the truncating allele is strong, the gene–phenotype match is strong, but phase is unproven and the second allele is a VUS. A value of 1.0 would claim certainty that the evidence does not support. It would also gain nothing — rank points depend on ordering, not on magnitude.

Remaining rows carry EPCR values between 0.02 and 0.20: enough to occupy rank positions 2–10, low enough not to degrade precision at the F-max optimum.

---

## 7\. Reproducibility

The repository contains the analysis scripts and an **evidence vault** in which every claim carries a verifiable identifier (PMID, DOI, HGNC, Ensembl, HPO) and a validator (`validar.py`) rejects any note asserting verification without a source.

Hypotheses are first-class objects with a mandatory falsification condition. **Refuted hypotheses are retained with the evidence that killed them** — including the authors' own initial hypothesis, which predicted that the causal variant would *not* be a straightforward finding in a known MVA gene. It was. The record of that error is kept deliberately.

## 8\. Data handling

No patient data is present in the public repository. The VCF, the phenotype document and all derived variant tables are held locally and excluded by `.gitignore`. A custody log records every environment the data has entered, so that the deletion required within 30 days of hackathon close can be certified.

---

## References

- Sieben CJ, Jeganathan KB, Nelson GG, et al. *BubR1 allelic effects drive phenotypic heterogeneity in mosaic-variegated aneuploidy progeria syndrome.* J Clin Invest. 2020;130(1):171-188. DOI:10.1172/JCI126863 · PMID:31738183 *(Metadata and abstract verified; full text not accessed. A published erratum (PMID:33136097) has not been reviewed — numeric values from the original are treated as provisional.)*  
- HGNC: *BUB1B* HGNC:1149 · *CEP57* HGNC:30794 · *TRIP13* HGNC:12307  
- Ensembl REST API (GRCh38) — gene coordinates and VEP annotation  
- Richards S, et al. *Standards and guidelines for the interpretation of sequence variants.* Genet Med. 2015\. PMID:25741868

---

*This report describes a computational analysis. It is not medical advice, a clinical diagnosis, or a recommendation for patient care.*  
