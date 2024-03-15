'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # unoptimised recursive solution
        # if n <=1:
        #     return 1
        # return climbStaris(n-1) + climbStairs(n-2)

        # optimized tabulation approach
        # Recursive problems can usually be solved using dp concepts
        if n<=1:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]