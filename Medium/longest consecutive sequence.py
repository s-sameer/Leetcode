'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        longest = 0
        
        for num in nums:
            if (num-1) not in myset:
                length = 0
                while (num+length) in myset:
                    length += 1
                longest = max(length, longest)
        
        return longest
