'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
# Intuition: two conditions to check if the parenthesis is valid
# 1. can only add closing parenthesis if the number of closing parenthesis is less than the number of opening parenthesis
# 2. can only add openining parenthesis if number of opening parenthesis is less than n
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()
        
        backtrack(0,0)
        return res
