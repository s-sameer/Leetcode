'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()
        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return 
            if total > target or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i+1, total+candidates[i])
            cur.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total)
        
        dfs(0, 0)
        return res