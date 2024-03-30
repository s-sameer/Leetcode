'''
Reverse bits of a given 32 bits unsigned integer.
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1
            res = res | (n & 1)
            n >>= 1
        return res