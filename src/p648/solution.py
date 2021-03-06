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


class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        result = []
        trie = Trie()
        for word in dict:
            trie.add(word)
        for word in sentence.split():
            root = trie.search(word)
            result.append(word if root is None else root)
        return ' '.join(result)
