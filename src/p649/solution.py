class Solution:
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        import collections
        q = collections.deque()
        P = [0, 0]
        ban = [0, 0]
        for c in senate:
            x = c == 'D'
            P[x] += 1
            q.append(x)

        while all(P):
            x = q.popleft()
            P[x] -= 1
            if ban[x] > 0:
                ban[x] -= 1
            else:
                ban[x^1] += 1
                q.append(x)
                P[x] += 1
        return 'Radiant' if P[0] != 0 else 'Dire'
