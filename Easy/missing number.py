'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''
# Intuition: sum numbers from 0 to n, then subtract the sum of the array
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      res = len(nums) #loop only creates numbers from 0 to n-1, that's why we need this
      for i in range(len(nums)):
        res += (i-nums[i])
      return res  