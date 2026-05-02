"""
Valid Sudoku
Medium
Topics
Company Tags
Hints
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:



Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true
Example 2:

Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false
Explanation: There are two 1's in the top-left 3x3 sub-box.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_list(row):
            valid = ["1","2","3","4","5","6","7","8","9"]
            for element in valid:
                counter = 0
                for anwser in row:
                    if element == anwser:
                        counter += 1
                if counter >1:
                    return False
            return True
            ##row.sort()
            #if valid == row:
            #    return True
            #else:
            #    return False
        columns = []
        for i in range(9):
            column = []
            for row in board:
                column.append(row[i])
            columns.append(column)


        #valid square
        split_rows = []
        for row in board:
            split_rows.extend([row[i:i+3] for i in range(0, len(row), 3)])

        squares = [[] for _ in range(9)]
        j = 0
        for i in range(9):
            if i<3:
                j = i
            elif i>2 and i<6:
                j = i + 6
            else:
                j = i + 12
            squares[i].extend(split_rows[j]) # i, i+3, i+6 == 0(0, 3, 6), 1(1, 4, 7), 2(2, 5, 8), 3(9, 12, 15), 4(10, 13, 16), 5(11, 14, 17)
            squares[i].extend(split_rows[j+3])
            squares[i].extend(split_rows[j+6])

        for n in range(9):
            r = valid_list(board[n])
            c = valid_list(columns[n])
            s = valid_list(squares[n])
            if not (r and c and s):
                return False
        return True

if __name__ == "__main__":
    board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
    new = Solution()
    print(new.isValidSudoku(board))
