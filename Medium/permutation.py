'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        per = []
        
        def dfs():
            if len(per) == len(nums):
                res.append(per.copy())
                return
            for i in range(len(nums)):
                if nums[i] in per:
                    continue
                else:
                    per.append(nums[i])
                    dfs()
                    per.remove(nums[i])
        
        dfs()
        return res
