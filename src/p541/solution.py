class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        r = ""
        for i in range(0, len(s), 2 * k):
            r += s[i:i + k][::-1]
            r += s[i + k:i + 2 * k]
        return r
