'''
Reverse bits of a given 32 bits unsigned integer.
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32): # iterate 32 times bc 32 bits
            res <<= 1 # shift res to the left by 1 bit to make room for the next bit
            res = res | (n & 1) # add the last bit of n to res
            n >>= 1 # shift n to the right by 1 bit to get the next bit
        return res
    
# We need to shift before adding the next bit and not after adding it bc it will result in a extra 0 at the end of res