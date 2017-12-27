from .mtbparser_exception import MTBParserException
from enum import Enum
from .snv_item import SNVItem

class SnvParser:
    """
    A parser class for somatic SNVs and small indels
    as part of the Molecular Tumor Board data
    provisioning in tumor diagnostics.
    Please check the documentation of this module in order
    to find out the exact file format specification.
    """
    def __init__(self, snv_file):
        self._header_to_column_mapping = {}
        self._path_to_snv_file = snv_file
        self._snv_list = []

        with open(snv_file, "r") as fh:
            lines = fh.readlines()
        if not lines:
            raise MTBParserException("Parsing failed: File was empty!")
        header = lines[0]
        self._parse_header(header)
        self._parse_content(lines)

    def _parse_header(self, header_string):
        """
        Parses the header and determines the column type
        and its column index.
        """
        header_content = header_string.strip().split('\t')
        if len(header_content) != SnvHeader.HEADER_LEN.value:
            raise MTBParserException(
                "Only {} header columns found, 12 expected!"
                .format(len(header_content)))
        counter = 0
        for column in header_content:
            for enum_type in SnvHeader:
                if column == enum_type.value:
                    self._header_to_column_mapping[enum_type.name] = counter
                    continue
            counter+=1

        if len(self._header_to_column_mapping) != SnvHeader.HEADER_LEN.value:
            debug_string = self._header_to_column_mapping.keys()
            raise MTBParserException("Parsing incomplete: Not all columns have been "
                    "matched to speficied column types. Identified {} columns, but expected {}. {}"
                    .format(len(self._header_to_column_mapping), SnvHeader.HEADER_LEN.value, debug_string))

    def _parse_content(self, snv_entries):
        """
        Parses SNV entries to SNVItems, objects
        representing the content for every entry, that
        can be used for further processing.
        """
        if len(snv_entries) == 1:
            return
        for line in snv_entries[1:]:
            self._snv_list.append(SNVItem(**self._header_to_column_mapping))

    def getSNVs(self):
        """
        Retrieve all parsed SNVItems.
        """
        return self._snv_list

class SnvHeader(Enum):
    """
    Enumeration class for the different column types
    specified in the header of the SNV tsv file.
    """
    CHR = "chr"
    START = "start"
    REF = "ref"
    ALT = "alt"
    ALLELE_F_TUMOR = "allele_frequency_tumor"
    COVERAGE = "coverage"
    GENE = "gene"
    BASE_CHANGE = "base_change"
    AA_CHANGE = "aa_change"
    TRANSCRIPT = "transcript"
    FUN_CLASS = "functional_class"
    EFFECT = "effect"
    HEADER_LEN = 12
