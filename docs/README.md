# Documentation

## File Formats

In total, this module provides parsers for **four** different information formats, that have been specified for data provisioning to the Molecular Tumor Board.

Formats for:

* [Somatic SNVs](./somatic_snvs.md)
* [Somatic CNVs](./cnvs.md)
* [Somatic structural variants](./structural_variants.md)
* [Germline SNVs](./germline_snvs.md)
* [Germline CNVs](./cnvs.md)
* [Metadata](./metadata.md)

All file formats are **tab separated** (tsv).

## Parser Classes

With respect to the format definitions, these parsers are available in ``mtbparser``:

* SNVParser