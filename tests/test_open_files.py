import os
import unittest
from nose.tools import raises
from mtbparser.snv_parser import SnvParser
from mtbparser.mtbparser_exception import MTBParserException

current_wd = os.path.dirname(__file__)

# A SNV tsv with a wrong header
test_wrong_header_file_loc = os.path.join(current_wd, "testfiles/ex_somatic_snvs_wrong_header.tsv")
# A working SNV tsv file
test_file_loc = os.path.join(current_wd, "testfiles/ex_somatic_snvs.tsv")
# A none existing path
test_wrong_file_loc = os.path.join(current_wd, "testfiles/not_present.tsv")
# An empty file
test_empty_file_loc = os.path.join(current_wd, "testfiles/ex_empty_file.tsv")

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
