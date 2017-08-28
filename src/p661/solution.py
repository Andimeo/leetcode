class Solution:
    @staticmethod
    def make_averager():
        count = 0
        total = 0

        def averager(new_value):
            nonlocal count, total
            count += 1
            total += new_value
            return total // count

        return averager

    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        N = [[0] * len(M[0]) for _ in range(len(M))]
        dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        for i in range(len(M)):
            for j in range(len(M[i])):
                avg = Solution.make_averager()
                for k in range(9):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < len(M) and 0 <= ny < len(M[i]):
                        N[i][j] = avg(M[nx][ny])
        return N
