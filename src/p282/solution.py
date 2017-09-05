class Solution(object):
    def add_expressions(self, pos, exp):
        if pos == len(self.nums) - 1:
            exp += self.nums[-1]
            self.expressions.append(exp)
            return
        for c in '+-*':
            self.add_expressions(pos + 1, exp + self.nums[pos] + c)

    def DFS(self, num, pos):
        if pos == len(num):
            self.add_expressions(0, '')
            return
        for i in range(pos, len(num)):
            self.nums.append(num[pos:i + 1])
            self.DFS(num, i + 1)
            self.nums.pop()

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.nums = []
        self.expressions = []
        self.DFS(num, 0)
        return filter(lambda x: eval(x) == target, self.expressions)
