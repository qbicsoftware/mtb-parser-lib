# Documentation

## File Formats

In total, this module provides parsers for **four** different information formats, that have been specified for data provisioning to the Molecular Tumor Board.

Formats for:

* [Somatic SNVs](./somatic_snvs.md)
* Somatic CNVs
* Somatic structural variants
* Germline SNVs
* Germline CNVs
* Metadata

All file formats are **tab separated** (tsv).

## Parser Classes

With respect to the format definitions, these parsers are available in ``mtbparser``:

* SNVParser