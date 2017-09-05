class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        stack = collections.deque()
        result, number, sign = 0, 0, 1
        for c in s:
            if c.isdigit():
                number = number * 10 + ord(c) - ord('0')
            elif c in '+-':
                result += sign * number
                number = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                result, number, sign = 0, 0, 1
            elif c == ')':
                result += sign * number
                result *= stack.pop()
                result += stack.pop()
        if number:
            result += number
        return result
