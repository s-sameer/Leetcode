'''
Write a function that takes the binary representation of a positive integer and returns the number of 
set bits it has (also known as the Hamming weight).
A set bit is a bit with value 1. A clear bit is a bit with value 0.
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binRep = bin(n)[2:]
        return binRep.count('1')

        # return n.bit_count() --> one liner
