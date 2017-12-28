"""
Test class suite for SNVItem objects
"""

import os
import unittest
from mtbparser.snv_parser import SnvParser
from mtbparser.snv_utils import SSnvHeader

CURRENT_WD = os.path.dirname(__file__)

# A loaded SNV file
TEST_LOADED_FILE_LOC = os.path.join(CURRENT_WD, "testfiles/somatic_snvs/ex_somatic_snvs_loaded.tsv")

class SnvItemTest(unittest.TestCase):
    """
    Sets up different test cases for the SNVItem class
    """
    def setUp(self):
        self._snv_parser_instance = SnvParser(TEST_LOADED_FILE_LOC, SSnvHeader)
        self._snv_item = self._snv_parser_instance.getSNVs()[1]

    def test_retrieve_attribute_from_snv(self):
        """Try to access attributes from parsed SNVItems"""
        snv_list = self._snv_parser_instance.getSNVs()
        assert len(snv_list) == 2, "Expected twoSNV items, but found %r" % len(snv_list)
        snv_example = snv_list[1]
        snv_gene = snv_example.get_snv_info(SSnvHeader.GENE.name)
        assert snv_gene == "BCRA1", "Expected gene name BCRA1, but was %r" % snv_gene

    def test_access_non_present_attribute(self):
        assert not self._snv_item.get_snv_info("AGE")

