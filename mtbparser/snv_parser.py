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
        with open(snv_file, "r") as fh:
            lines = fh.readlines()
        if not lines:
            raise MTBParserException("Parsing failed: File was empty!")
        header = lines[0]
        self._check_header(header)


    def _check_header(self, header_string):
        header_content = header_string.split('\t')
        if len(header_content) != 12:
            print(header_content)
            raise MTBParserException(
                "Only {} header columns found, 12 expected!"
                .format(len(header_content)))