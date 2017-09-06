class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n, m = len(dungeon), len(dungeon[0])
        d = [[-1] * m for _ in range(n)]
        dx, dy = [1, 0], [0, 1]

        # It's correct traversing from bottom-right to up-left
        # It's wrong the other way around
        def dp(x, y):
            if d[x][y] != -1:
                return d[x][y]
            if x == n - 1 and y == m - 1:
                d[x][y] = max(1, 1 - dungeon[x][y])
                return d[x][y]
            for i in range(2):
                nx, ny = x + dx[i], y + dy[i]
                if nx < n and ny < m:
                    dn = max(1, dp(nx, ny) - dungeon[x][y])
                    if d[x][y] == -1 or d[x][y] > dn:
                        d[x][y] = dn
            return d[x][y]

        ans = dp(0, 0)
        return ans
