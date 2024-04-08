'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
# Intuition: We can use hashmap and set to store the numbers in each row, column and sub-boxes. 
# The row/col index is used as the key in the hashmap and the set stores the numbers in that row/col
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subboxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    if (board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in subboxes[(r//3, c//3)]):
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    subboxes[(r//3, c//3)].add(board[r][c])
        return True