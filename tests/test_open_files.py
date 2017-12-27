import unittest
from nose.tools import assert_raises

test_file_loc = "testfiles/ex_somatic_snvs.tsv"
test_wrong_file_loc = "testfiles/not_present.tsv"

class BasicTests(unittest.TestCase):

    def test_try_to_read_from_file(self):
        with assert_raises(IOError):
            SnvParser(test_wrong_file_loc)
    

