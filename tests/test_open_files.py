import os
import unittest
from nose.tools import raises
from mtbparser.snv_parser import SnvParser
from mtbparser.mtbparser_exception import MTBParserException

current_wd = os.path.dirname(__file__)

test_file_loc = os.path.join(current_wd, "testfiles/ex_somatic_snvs.tsv")
test_wrong_file_loc = os.path.join(current_wd, "testfiles/not_present.tsv")

class BasicTests(unittest.TestCase):

    @raises(IOError, MTBParserException)
    def test_try_to_read_from_none_existing_file(self):
        SnvParser(test_wrong_file_loc)

    # This should always work
    def test_try_to_read_from_existing_file(self):
        SnvParser(test_file_loc)
    

