'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
# Intuition: sort the array, pick one element and then use two pointer approach to find the other two elements.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)-2):
            num = nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                total = num + nums[left] + nums[right]
                if total < 0:
                    left = left + 1
                elif total > 0:
                    right = right - 1
                else:
                    # once valid triplet is found, add it to the set and move both the pointers to find other triplets
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        return [list(triplet) for triplet in res]