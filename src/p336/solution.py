class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        d = {word: i for i, word in enumerate(words)}
        l = []
        for index, word in enumerate(words):
            if '' in d and d[''] != index and word == word[::-1]:
                l.append([d[''], index])
            for i in range(len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix == prefix[::-1] and suffix[::-1] in d and d[suffix[::-1]] != index:
                    l.append([d[suffix[::-1]], index])
                if suffix == suffix[::-1] and prefix[::-1] in d and d[prefix[::-1]] != index:
                    l.append([index, d[prefix[::-1]]])
        return l
