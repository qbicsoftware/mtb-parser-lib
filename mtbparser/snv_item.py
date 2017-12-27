from .snv_utils import SnvHeader
from .mtbparser_exception import MTBSnvFormatException

class SNVItem():

    def __init__(self, **info):
        self._snv_info = self._format_dict(info)

    def _format_dict(self, info_dict):
        """Replaces empty content with 'NA's"""
        for key, value in info_dict.items():
            if not value:
                info_dict[key] = "NA"
        return info_dict

    def get_snv_info(self):
        return self._snv_info
    
