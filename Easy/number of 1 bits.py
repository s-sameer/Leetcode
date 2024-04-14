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
    
        # Alternate solution, no built-in functions
        # res = 0
        # while n:
        #     res += n & 1
        #     n >>= 1
        # return res

        # algorithm for converting decimal to binary
        def decimal_to_binary(n):
            binary = ''
            while n > 0:
                binary = str(n % 2) + binary
                n = n // 2
            return binary
