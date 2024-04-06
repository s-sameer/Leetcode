'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        # find the row containing the target
        top, bottom = 0, ROWS - 1
        while top <= bottom:
            mid = (top + bottom)//2
            if target > matrix[mid][-1]: #if target is greater than the last element of the mid point
                top = mid + 1
            elif target < matrix[mid][0]: #if target is smaller than the first element of the mid point
                bottom = mid - 1
            else: #if target is in the mid point
                break
        
        if top > bottom: 
            return False
        
        mid = (top + bottom)//2
        # find the column containing the target
        left, right = 0, COLS - 1
        while left <= right:
            m = (left + right)//2
            if target > matrix[mid][m]:
                left = m + 1
            elif target < matrix[mid][m]:
                right = m - 1
            else:   
                return True
            