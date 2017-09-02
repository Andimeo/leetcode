class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        n = len(machines)
        sum_n = sum(machines)
        if sum_n % n != 0:
            return -1
        avg = sum_n // n
        balance = [x - avg for x in machines]
        result = 0
        tmp = 0
        for b in balance:
            tmp += b
            # 当b < 0时，不需要求abs，因为abs(tmp)已经包含了b的绝对值，若两边
            # 都需要往b送衣服，则可以同时发生，若只有右边需要往b送衣服，则abs(b) == abs(tmp)
            # 而当b > 0时，有可能b要同时往两边送衣服，而这个行为不能同时发生，所以需要单独计算
            # 因为abs(tmp)小于b时，b需要往两边送，不能被abs(tmp)覆盖
            result = max(result, b, abs(tmp))
        return result
