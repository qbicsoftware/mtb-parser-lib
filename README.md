# qbic.mtbparser

[![Build status](https://travis-ci.org/qbicsoftware/qbic.mtbparser.svg?branch=development)](https://travis-ci.org/qbicsoftware/qbic.mtbparser/) [![codecov](https://codecov.io/gh/qbicsoftware/qbic.mtbparser/branch/development/graph/badge.svg)](https://codecov.io/gh/qbicsoftware/qbic.mtbparser/)

A simple module that provides parser for different diagnostic variant information as part of the Molecular Tumor Board data provisioning in Tübingen.

## Documentation

File formats for
* [Somatic SNVs](./docs/somatic_snvs.md)
* [Somatic CNVs](./docs/cnvs.md)
* [Somatic structural variants](./docs/structural_variants.md)
* [Germline SNVs](./docs/germline_snvs.md)
* [Germline CNVs](./docs/cnvs.md)
* [Metadata](./docs/metadata.md)

Python class info
* SnvParser

### How to use the SnvParser class

Parsing a SNV file following the formats described above is fairly simple. Just create an ``SnvParser`` object with the path to the ``tsv``-file and specify its type by providing the correct header (``SSnvHeader, GSnvHeader, ...``).

```python
from mtbparser.snv_parser import SnvParser
from mtbparser.snv_utils import SSnvHeader

# Path to a valid SNV tsv file, as specified in
# the file format documentation.
somatic_snv_file = "/path/to/mySSnv.tsv"

# Create parser object for somatic SNVs
parser = SnvParser(somatic_snv_file, SSnvHeader)

# Iterate through parsed SNV items and get the gene name
for snv_item in parser.getSNVs():
    print(snv_item.get_snv_info(SSnvHeader.GENE.name))
```


## Author
This code implementation was done at the [Quantitative Biology Center](http://qbic.life). Please contact the author [@sven1103](https://github.com/sven1103) for more information.
