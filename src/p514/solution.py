class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        import collections
        pos = collections.defaultdict(list)
        alphas = set(key)
        for i, c in enumerate(ring):
            if c in alphas:
                pos[c].append(i)

        memo = [{} for _ in range(len(key))]

        # index is the current position in key
        # pos_in_ring is the corresponding position in ring
        def dp(index, pos_in_ring):
            assert ring[pos_in_ring] == key[index]
            if pos_in_ring in memo[index]:
                return memo[index][pos_in_ring]
            if index == 0:
                memo[index][pos_in_ring] = min(pos_in_ring, len(ring) - pos_in_ring) + 1
                return memo[index][pos_in_ring]
            result = len(ring) * len(key)
            c = key[index - 1]
            for p in pos[c]:
                t = abs(pos_in_ring - p)
                result = min(result, dp(index - 1, p) + min(t, len(ring) - t) + 1)
            memo[index][pos_in_ring] = result
            return result

        result = len(ring) * len(key)
        for p in pos[key[-1]]:
            result = min(result, dp(len(key) - 1, p))
        return result
