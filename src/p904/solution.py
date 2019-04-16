class Solution:
    def totalFruit(self, tree) -> int:
        b = 0
        s = {tree[0]:1}
        result = 1
        r = 1
        for i in range(1, len(tree)):
            if tree[i] not in s:
                s[tree[i]] = 1
            else:
                s[tree[i]] += 1
            r += 1
            if len(s) <= 2:
                result = max(result, r)
            while len(s) > 2:
                s[tree[b]] -= 1
                if s[tree[b]] == 0:
                    del s[tree[b]]
                b += 1
                r -= 1
        return result
