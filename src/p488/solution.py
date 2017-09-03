class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        import collections
        counter = collections.Counter(hand)
        board += '#'

        def DFS(board):
            board = remove(board)
            if board == '#':
                return 0
            i = 0
            result = 6
            for j in range(len(board)):
                if board[i] == board[j]:
                    continue
                num = 3 - (j - i)
                if counter[board[i]] >= num:
                    counter[board[i]] -= num
                    result = min(result, num + DFS(board[:i] + board[j:]))
                    counter[board[i]] += num
                i = j
            return result

        def remove(board):
            i = 0
            for j in range(len(board)):
                if board[j] == board[i]:
                    continue
                num = j - i
                if num >= 3:
                    l = board[:i] + board[j:]
                    return remove(l)
                else:
                    i = j
            return board

        result = DFS(board)
        return -1 if 6 == result else result
