class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {'A': 0, 'T': 1, 'C': 2, 'G': 3}
        num = 0
        t = set()
        result = set()
        for i, c in enumerate(s):
            if i > 9:
                num -= 4 ** 9 * d[s[i - 10]]
            num = num * 4 + d[c]
            if i > 8:
                if num in t:
                    result.add(s[i - 9:i + 1])
                else:
                    t.add(num)
        return list(result)
