class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for m in moves:
            if m == 'U':
                x += 1
            if m == 'D':
                x -= 1
            if m == 'L':
                y -= 1
            if m == 'R':
                y += 1
        return (x, y) == (0, 0)
