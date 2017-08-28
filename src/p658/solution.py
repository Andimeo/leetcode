class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        import bisect
        arr = [-0x0fffffff] + arr + [0x0fffffff]
        pos = bisect.bisect(arr, x)
        left, right = pos - 1, pos
        result = []
        while len(result) < k:
            if x - arr[left] > arr[right] - x:
                result.append(arr[right])
                right += 1
            else:
                result.append(arr[left])
                left -= 1
        result.sort()
        return result
