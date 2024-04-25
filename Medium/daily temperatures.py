'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait 
after the ith day to get a warmer temperature. 3If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                index, temp = stack.pop()
                res[index] = i - index
            stack.append((i,t))
        
        return res