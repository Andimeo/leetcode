class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = []
        for i in range(32):
            bits.append(n & 1)
            n >>= 1
        result = 0
        for bit in bits:
            result = result * 2 + bit
        return result
