class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        import collections
        d = collections.defaultdict(list)
        result = []
        for i, word in enumerate(words):
            l = d[word[::-1]]
            for pos in l:
                result.append([pos, i])
                result.append([i, pos])
            d[word].append(i)
        return result
