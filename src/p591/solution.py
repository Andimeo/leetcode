import re


class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        if code == 't':
            return False
        code = re.sub('<!\[CDATA\[.*?\]\]>', 'c', code)
        prev = ''
        while code != prev:
            prev = code
            code = re.sub('<([A-Z]{1,9})>[^<]*</\\1>', 't', code)
        return code == 't'
