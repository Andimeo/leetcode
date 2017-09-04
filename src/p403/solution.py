class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        d = {}
        for i, stone in enumerate(stones):
            d[stone] = i

        n = len(stones)
        if stones[1] != 1:
            return False
        memo = [set() for _ in range(n)]
        memo[1].add(1)
        for i in range(1, n):
            for step in memo[i]:
                for k in range(step - 1, step + 2):
                    if stones[i] + k in d:
                        pos = d[stones[i] + k]
                        memo[pos].add(k)
        return len(memo[n - 1]) > 0
