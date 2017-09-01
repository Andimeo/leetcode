class Solution(object):
    """
    http://www.lydxlx.net/2017/03/26/first-post/
    """

    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(boxes)
        memo = {}

        def dp(left, right, extra_length):
            if left > right:
                return 0
            if (left, right, extra_length) in memo:
                return memo[left, right, extra_length]

            index = right
            while boxes[index] == boxes[right] and index >= left:  # for speeding up
                index -= 1
            ans = dp(left, index, 0) + (extra_length + right - index) ** 2
            for i in range(left, index):
                if boxes[i] == boxes[right]:
                    ans = max(ans, dp(left, i, extra_length + right - index) + dp(i + 1, index, 0))
            memo[left, right, extra_length] = ans
            return ans

        return dp(0, n - 1, 0)
