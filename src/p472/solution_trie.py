class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = TrieNode()
                node = node.children[c]
        node.is_end = True

    def exist(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    def search(self, word):
        node = self.root
        l = []
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
            l.append(c)
            if node.is_end:
                return ''.join(l)
        return None


class TrieNode:
    def __init__(self, is_end=False):
        self.is_end = is_end
        self.children = {}


class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words = list(set(words))
        words.sort(key=lambda word: (len(word), word))
        self.trie = Trie()
        result = []
        for word in words:
            if self.exist(word, 0, 0):
                result.append(word)
            self.trie.add(word)
        return result

    def exist(self, word, cur, cnt):
        if cur == len(word):
            return cnt > 1
        for i in range(len(word) + 1, cur, -1):
            if self.trie.exist(word[cur:i]) and self.exist(word, i, cnt + 1):
                return True
        return False
