class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def is_valid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                if c == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        queue = {s}
        while True:
            valid_set = filter(is_valid, queue)
            if valid_set:
                return list(valid_set)
            queue = {s[:i] + s[i + 1:] for s in queue for i in range(len(s))}
