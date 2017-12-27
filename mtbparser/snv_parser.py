from .mtbparser_exception import MTBParserException

class SnvParser:
    """
    A parser class for somatic SNVs and small indels
    as part of the Molecular Tumor Board data
    provisioning in tumor diagnostics.
    Please check the documentation of this module in order
    to find out the exact file format specification.
    """
    path_to_snv_file = ""

    def __init__(self, snv_file):
        self.path_to_snv_file = snv_file
        try:
            with open(snv_file, "r") as fh:
                pass
        except IOError as err:
            raise MTBParserException("Parsing failed because SNV file was not accessible.")
            raise IOError(err)

