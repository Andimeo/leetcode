class Solution:
    # https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nodes = []
        num, cnt = None, None
        for i in range(len(nums)):
            if i == 0:
                num, cnt = nums[i], 1
                continue
            if nums[i] != nums[i - 1]:
                nodes.append((num, cnt))
                num, cnt = nums[i], 1
            else:
                cnt += 1
        nodes.append((num, cnt))

        pre, p1, p2, p3 = 0xffffffff, 0, 0, 0
        for node in nodes:
            num, cnt = node
            c1, c2, c3 = 0, 0, 0
            if num != pre + 1:
                if p1 != 0 or p2 != 0:
                    return False
                c1, c2, c3 = cnt, 0, 0
            else:
                if cnt < p1 + p2:
                    return False
                c2 = p1
                c3 = p2 + min(p3, cnt - p2 - p1)
                c1 = max(0, cnt - p1 - p2 - p3)
            pre, p1, p2, p3 = num, c1, c2, c3
            # print(num, cnt, c1, c2, c3)
        return p1 == 0 and p2 == 0
