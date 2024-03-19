'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        noDup = list(set(nums))
        if len(noDup) < len(nums):
            return True
        else:
            return False
        