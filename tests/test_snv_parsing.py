import os
import unittest
from nose.tools import raises
from mtbparser.snv_parser import SnvParser
from mtbparser.mtbparser_exception import MTBParserException
from mtbparser.snv_utils import SSnvHeader
from mtbparser.snv_utils import GSnvHeader

CURRENT_WD = os.path.dirname(__file__)

# A SNV tsv with a wrong header
TEST_WRONG_HEADER_FILE_LOC = os.path.join(CURRENT_WD, "testfiles/somatic_snvs/ex_somatic_snvs_wrong_header.tsv")
# A working SNV tsv file
TEST_FILE_LOC = os.path.join(CURRENT_WD, "testfiles/somatic_snvs/ex_somatic_snvs.tsv")
# A none existing path
TEST_WRONG_FILE_LOC = os.path.join(CURRENT_WD, "testfiles/somatic_snvs/not_present.tsv")
# An empty file
TEST_EMPTY_FILE_LOC = os.path.join(CURRENT_WD, "testfiles/ex_empty_file.tsv")
# A loaded SNV file
TEST_LOADED_FILE_LOC = os.path.join(CURRENT_WD, "testfiles/somatic_snvs/ex_somatic_snvs_loaded.tsv")
# A corrupted SNV file
TEST_CORRUPTED_FILE_LOC = os.path.join(CURRENT_WD, "testfiles/somatic_snvs/ex_somatic_snvs_loaded_corrupt.tsv")
# A SNV file with a truncated header
TEST_TRUNCATED_HEADER_LOC = os.path.join(CURRENT_WD, "testfiles/somatic_snvs/ex_somatic_snvs_trunc_header.tsv")
# A loaded germline SNV
TEST_LOADED_GNVS_LOC = os.path.join(CURRENT_WD, "testfiles/germline_snvs/ex_germline_snvs_loaded.tsv")

class BasicTests(unittest.TestCase):

    @raises(IOError)
    def test_try_to_read_from_none_existing_file(self):
        SnvParser(TEST_WRONG_FILE_LOC, SSnvHeader)

    def test_try_to_read_from_existing_file(self):
        SnvParser(TEST_FILE_LOC, SSnvHeader)

    @raises(MTBParserException)
    def test_read_from_empty_file(self):
        SnvParser(TEST_EMPTY_FILE_LOC, SSnvHeader)

    @raises(MTBParserException)
    def test_parse_header_from_corrupted_file(self):
        SnvParser(TEST_WRONG_HEADER_FILE_LOC, SSnvHeader)

    def test_parse_header_from_file(self):
        SnvParser(TEST_FILE_LOC, SSnvHeader)

    def test_parse_content_empty(self):
        snv_list = SnvParser(TEST_FILE_LOC, SSnvHeader).getSNVs()
        assert not snv_list, "List was not empty but %r" % len(snv_list)
    
    def test_parse_loaded_snv_file(self):
        snv_list = SnvParser(TEST_LOADED_FILE_LOC, SSnvHeader).getSNVs()
        assert len(snv_list) == 2, "Expected number of SNV elements was 2, but found %r" % len(snv_list)

    @raises(MTBParserException)
    def test_parse_corrupted_snv_file(self):
        snv_list = snv_list = SnvParser(TEST_CORRUPTED_FILE_LOC, SSnvHeader).getSNVs()

    @raises(MTBParserException)
    def test_parse_truncated_header(self):
        SnvParser(TEST_TRUNCATED_HEADER_LOC, SSnvHeader)

    def test_parse_content_gsnv(self):
        SnvParser(TEST_LOADED_GNVS_LOC, GSnvHeader)

    @raises(MTBParserException)
    def test_load_wrong_enum_for_file_type(self):
        SnvParser(TEST_FILE_LOC, GSnvHeader)
