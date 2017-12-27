# qbic-mtbparser

[![Build status](https://travis-ci.org/qbicsoftware/qbic-centraxx-mtb-wf.svg?branch=development)](https://travis-ci.org/qbicsoftware/qbic-centraxx-mtb-wf/) [![codecov](https://codecov.io/gh/qbicsoftware/qbic-centraxx-mtb-wf/branch/development/graph/badge.svg)](https://codecov.io/gh/qbicsoftware/qbic-centraxx-mtb-wf)


A simple module that provides parser for different diagnostic variant information as part of the Molecular Tumor Board data provisioning in Tübingen.

## The SnvParser class
This class parses a SNV file (tsv format!) of the following specified format. Be aware that each of the following listings represent a **tab-separated** column field in the input SNV file:

* [chr](#chr)
* [start](#start)
* [ref](#ref)
* [alt](#alt)
* [allele\_frequency\_tumor](#all_f)
* [coverage](#coverage)
* [base_change](#base)
* [aa_change](#aa)
* [transcript](#transcript)
* [functional\_class](#fclass)
* [effect](effect)

---

### <a name="chr"></a>'chr'
The chromosome location of the variant.

**Example**

``chr: chr1``

---

### <a name="start"></a>'start'
The genomic start position of the variant.

**Example**

``start: 12500``

---

### <a name="ref"></a>'ref'
The reference base at this position.

**Example**


``ref: C``

---

### <a name="alt"></a>'alt'
The altered base et this position.

**Example**

``alt: G``

---

### <a name="all_f"></a>'allele\_frequency\_tumor'
The allele frequence of the variant in the tumor.

**Example**

``allele_frequency_tumor: 0.25``

---

### <a name="coverage"></a>'coverage'
The read coverage mapped at this position.

**Example**

``coverage: 100``

---

### <a name="gene"></a>'gene'
[HGNC](https://www.genenames.org) formatted gene name.

**Example**

``gene: tumor protein p53``

---

### <a name="base"></a>'base_change'
[HGVS](http://varnomen.hgvs.org/recommendations/DNA/) formatted base change.

**Example**

``base_change: g.123A>G``

---

### <a name="aa"></a>'aa_change'
[HGVS](http://varnomen.hgvs.org/recommendations/protein/) formatted amino acid change.

**Example**

``aa_change: Arg54Ser``

---

### <a name="transcript"></a>'transcript'
Transcript reference identifier. Refseq or Ensembl.

**Example**

``transcript: NM_001143990.1``

---

### <a name="fclass"></a>'functional\_class'
The functional class of the variant in Sequence Onthology terms.

**Example**

``functional_class: intron_variant``

---

### <a name="effect"></a>'effect'
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

