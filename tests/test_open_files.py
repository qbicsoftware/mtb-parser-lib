import os
import unittest
from nose.tools import raises
from mtbparser.snv_parser import SnvParser
from mtbparser.mtbparser_exception import MTBParserException

current_wd = os.path.dirname(__file__)

# A SNV tsv with a wrong header
test_wrong_header_file_loc = os.path.join(current_wd, "testfiles/somatic_snvs/ex_somatic_snvs_wrong_header.tsv")
# A working SNV tsv file
test_file_loc = os.path.join(current_wd, "testfiles/somatic_snvs/ex_somatic_snvs.tsv")
# A none existing path
test_wrong_file_loc = os.path.join(current_wd, "testfiles/somatic_snvs/not_present.tsv")
# An empty file
test_empty_file_loc = os.path.join(current_wd, "testfiles/ex_empty_file.tsv")
# A loaded SNV file
test_loaded_file_loc = os.path.join(current_wd, "testfiles/somatic_snvs/ex_somatic_snvs_loaded.tsv")
# A corrupted SNV file
test_corrupted_file_loc = os.path.join(current_wd, "testfiles/somatic_snvs/ex_somatic_snvs_loaded_corrupt.tsv")
# A SNV file with a truncated header
test_truncated_header_loc = os.path.join(current_wd, "testfiles/somatic_snvs/ex_somatic_snvs_trunc_header.tsv")

class BasicTests(unittest.TestCase):

    @raises(IOError)
    def test_try_to_read_from_none_existing_file(self):
        SnvParser(test_wrong_file_loc)

    def test_try_to_read_from_existing_file(self):
        SnvParser(test_file_loc)

    @raises(MTBParserException)
    def test_read_from_empty_file(self):
        SnvParser(test_empty_file_loc)

    @raises(MTBParserException)
    def test_parse_header_from_corrupted_file(self):
        SnvParser(test_wrong_header_file_loc)

    def test_parse_header_from_file(self):
        SnvParser(test_file_loc)

    def test_parse_content_empty(self):
        snv_list = SnvParser(test_file_loc).getSNVs()
        assert not snv_list, "List was not empty but %r" % len(snv_list)
    
    def test_parse_loaded_snv_file(self):
        snv_list = SnvParser(test_loaded_file_loc).getSNVs()
        assert len(snv_list) == 2, "Expected number of SNV elements was 2, but found %r" % len(snv_list)

    @raises(MTBParserException)
    def test_parse_corrupted_snv_file(self):
        snv_list = snv_list = SnvParser(test_corrupted_file_loc).getSNVs()

    @raises(MTBParserException)
    def test_parse_truncated_header(self):
        SnvParser(test_truncated_header_loc)
