from enum import Enum

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