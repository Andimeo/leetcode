class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        self.words = set(words)
        result = []
        for word in self.words:
            if self.exist(word, 0, 0):
                result.append(word)
        return result

    def exist(self, word, cur, cnt):
        if cur == len(word):
            return cnt > 1
        for i in range(len(word) + 1, cur, -1):
            if word[cur:i] in self.words and self.exist(word, i, cnt + 1):
                return True
        return False
