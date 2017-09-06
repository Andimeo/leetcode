class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        import collections
        counter = collections.Counter(secret)
        bull, cow = 0, 0
        for s, g in zip(secret, guess):
            if counter[g] > 0:
                if g == s:
                    bull += 1
                    counter[g] -= 1
        for s, g in zip(secret, guess):
            if counter[g] > 0:
                if g != s:
                    cow += 1
                    counter[g] -= 1
        return str(bull) + 'A' + str(cow) + 'B'
