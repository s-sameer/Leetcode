'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        The first thing that should come to your mind when searching for an
        element efficiently is binary search
        To find the first bad version, we need to find the bad version whose prev 
        element is not a bad version
        """
        low, high = 0, n
        while low <= high:
            mid = (low+high)//2
            prev = mid - 1
            if isBadVersion(mid) and not isBadVersion(prev):
                return mid
            elif isBadVersion(mid) and isBadVersion(prev):
                high = mid - 1
            else:
                low = mid + 1
            
    