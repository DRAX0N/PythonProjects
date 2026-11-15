"""
3963. Create Grid With Exactly One Path
Easy
premium lock icon
Companies
Hint
You are given two integers m and n, representing the number of rows and columns of a grid.

Construct any m x n grid consisting only of the characters '.' and '#', where:

'.' represents a free cell.
'#' represents an obstacle cell.
A valid path is a sequence of free cells that:

Starts at the top-left cell (0, 0).
Ends at the bottom-right cell (m - 1, n - 1).
Moves only:
Right, from (i, j) to (i, j + 1), or
Down, from (i, j) to (i + 1, j).
Return any grid such that there is exactly one valid path from the top-left cell to the bottom-right cell.

 

Example 1:

Input: m = 2, n = 3

Output: ["..#","#.."]

Explanation:



The only valid path is: (0,0) → (0,1) → (1,1) → (1,2)

Example 2:

Input: m = 3, n = 3

Output: ["..#","#..","##."]

Explanation:



The only valid path is: (0,0) → (0,1) → (1,1) → (1,2) → (2,2)

Example 3:

Input: m = 1, n = 4

Output: ["...."]

Explanation:

The only valid path is: (0,0) → (0,1) → (0,2) → (0,3)

 

Constraints:

1 <= m, n <= 25
"""


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Create an m x n grid filled with '#'
        grid = [['#' for _ in range(n)] for _ in range(m)]

        # Create a path from (0, 0) to (m - 1, n - 1)
        for i in range(m):
            grid[i][0] = '.'  # Fill the first column with '.'
        for j in range(1, n):
            grid[m - 1][j] = '.'  # Fill the last row with '.'

        # Convert each row to a string
        return [''.join(row) for row in grid]
    
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        arr = [("." + "#" * (n-1)) for i in range(m-1)]
        arr.append("."* n)

        
        return arr
    
if __name__ == "__main__":
    solution = Solution()
    m = 2
    n = 3
    print(solution.createGrid(m, n))  # Output: ["..#", "#.."]

    m = 3
    n = 3
    print(solution.createGrid(m, n))  # Output: ["..#", "#..", "##."]

    m = 1
    n = 4
    print(solution.createGrid(m, n))  # Output: ["...."]
