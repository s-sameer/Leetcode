'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
'''
# Intuition: Evalation of expressions typically involves a stack. We can use a stack to store the operands and evaluate the expression.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                total = num1 + num2
                stack.append(total)
            elif token == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                total = num2 - num1
                stack.append(total)
            elif token == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                total = num1 * num2
                stack.append(total)
            elif token == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                total = int(num2 / num1)
                stack.append(total)
            else:
                stack.append(int(token))
        
        return stack[0]