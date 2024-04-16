'''
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
'''
# Intuition: We can use backtracking to generate all possible subsets of the given array.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] #This will store all our subsets
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return res