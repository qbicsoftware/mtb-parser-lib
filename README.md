# qbic-mtbparser

[![Build status](https://travis-ci.org/qbicsoftware/qbic-centraxx-mtb-wf.svg?branch=development)](https://travis-ci.org/qbicsoftware/qbic-centraxx-mtb-wf/) [![codecov](https://codecov.io/gh/qbicsoftware/qbic-centraxx-mtb-wf/branch/development/graph/badge.svg)](https://codecov.io/gh/qbicsoftware/qbic-centraxx-mtb-wf)


A simple module that provides parser for different diagnostic variant information as part of the Molecular Tumor Board data provisioning in Tübingen.

## The SnvParser class
This class parses a SNV file (tsv format!) of the following specified format. Be aware that each of the following listings represent a **tab-separated** column field in the input SNV file:

* [chr](#chr)
* start
* ref
* alt
* allele\_frequency\_tumor
* coverage
* base_change
* aa_change
* transcript
* functional\_class
* effect

---

### <a name="chr"></a>'chr'
The chromosome location of the variant.

**Example**

``chr: chr1``

---

### 'start'
The genomic start position of the variant.

**Example**

``start: 12500``

---

### 'ref'
The reference base at this position.

**Example**


``ref: C``

---

### 'alt'
The altered base et this position.

**Example**

``alt: G``

---

### 'allele\_frequency\_tumor'
The allele frequence of the variant in the tumor.

**Example**

``allele_frequency_tumor: 0.25``

---

### 'coverage'
The read coverage mapped at this position.

**Example**

``coverage: 100``

---

### 'gene'
[HGNC](https://www.genenames.org) formatted gene name.

**Example**

``gene: tumor protein p53``

---

### 'base_change'
[HGVS](http://varnomen.hgvs.org/recommendations/DNA/) formatted base change.

**Example**

``base_change: g.123A>G``

---

### 'aa_change'
[HGVS](http://varnomen.hgvs.org/recommendations/protein/) formatted amino acid change.

**Example**

``aa_change: Arg54Ser``

---

### 'transcript'
Transcript reference identifier. Refseq or Ensembl.

**Example**

``transcript: NM_001143990.1``

---

### 'functional\_class'
The functional class of the variant in Sequence Onthology terms.

**Example**

``functional_class: intron_variant``

---

### 'effect'
The predicted or annotated effect of the variant. Currently an enumeration of:

* activating
* inactivating
* function_changed
* probably\_activating
* probably\_inactivating
* probably\_function\_change
* ambigious
* benign
* NA

**Example**

``effect: activating``

