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


class Solution(object):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    def DFS(self, i, j, trie_node, cur):
        if trie_node.is_end:
            self.result.add(cur)
        for k in range(4):
            nx, ny = i + self.dx[k], j + self.dy[k]
            if 0 <= nx < self.n and 0 <= ny < self.m and not self.visited[nx][ny] and self.board[nx][
                ny] in trie_node.children:
                self.visited[nx][ny] = 1
                self.DFS(nx, ny, trie_node.children[self.board[nx][ny]], cur + self.board[nx][ny])
                self.visited[nx][ny] = 0

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.n, self.m = len(board), len(board[0]) if len(board) > 0 else 0
        if not self.n or not self.m:
            return []
        self.board = board
        self.trie = Trie()
        for word in words:
            self.trie.add(word)

        self.result = set()
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] in self.trie.root.children:
                    self.visited = [[0] * self.m for _ in range(self.n)]
                    self.visited[i][j] = 1
                    self.DFS(i, j, self.trie.root.children[board[i][j]], board[i][j])
        return list(self.result)
