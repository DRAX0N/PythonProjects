"""
3665. Twisted Mirror Path Count
Medium
Topics
premium lock icon
Companies
Hint
Given an m x n binary grid grid where:

grid[i][j] == 0 represents an empty cell, and
grid[i][j] == 1 represents a mirror.
A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). It can move only right or down. If the robot attempts to move into a mirror cell, it is reflected before entering that cell:

If it tries to move right into a mirror, it is turned down and moved into the cell directly below the mirror.
If it tries to move down into a mirror, it is turned right and moved into the cell directly to the right of the mirror.
If this reflection would cause the robot to move outside the grid boundaries, the path is considered invalid and should not be counted.

Return the number of unique valid paths from (0, 0) to (m - 1, n - 1).

Since the answer may be very large, return it modulo 109 + 7.

Note: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.

 

Example 1:

Input: grid = [[0,1,0],[0,0,1],[1,0,0]]

Output: 5

Explanation:

Number	Full Path
1	(0, 0) → (0, 1) [M] → (1, 1) → (1, 2) [M] → (2, 2)
2	(0, 0) → (0, 1) [M] → (1, 1) → (2, 1) → (2, 2)
3	(0, 0) → (1, 0) → (1, 1) → (1, 2) [M] → (2, 2)
4	(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)
5	(0, 0) → (1, 0) → (2, 0) [M] → (2, 1) → (2, 2)
[M] indicates the robot attempted to enter a mirror cell and instead reflected.

Example 2:

Input: grid = [[0,0],[0,0]]

Output: 2

Explanation:

Number	Full Path
1	(0, 0) → (0, 1) → (1, 1)
2	(0, 0) → (1, 0) → (1, 1)
Example 3:

Input: grid = [[0,1,1],[1,1,0]]

Output: 1

Explanation:

Number	Full Path
1	(0, 0) → (0, 1) [M] → (1, 1) [M] → (1, 2)
(0, 0) → (1, 0) [M] → (1, 1) [M] → (2, 1) goes out of bounds, so it is invalid.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 500
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
"""
from typing import List

MOD = 10**9 + 7


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # f[i][j][0] = entered moving right, f[i][j][1] = entered moving down
        f = [[[0, 0] for _ in range(n)] for _ in range(m)]
        # start: treat as standing on (0,0), which is empty
        f[0][0][0] = 1

        for i in range(m):
            for j in range(n):
                r, d = f[i][j]
                if r == 0 and d == 0:
                    continue
                if i == m - 1 and j == n - 1:
                    break
                if grid[i][j] == 0:
                    total = (r + d) % MOD
                    if j + 1 < n:
                        f[i][j + 1][0] = (f[i][j + 1][0] + total) % MOD
                    if i + 1 < m:
                        f[i + 1][j][1] = (f[i + 1][j][1] + total) % MOD
                else:
                    # entered moving right -> deflected down
                    if r and i + 1 < m:
                        f[i + 1][j][1] = (f[i + 1][j][1] + r) % MOD
                    # entered moving down -> deflected right
                    if d and j + 1 < n:
                        f[i][j + 1][0] = (f[i][j + 1][0] + d) % MOD

        return (f[m - 1][n - 1][0] + f[m - 1][n - 1][1]) % MOD
    
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        curRow = [0] * n
        curRow[0] = 1
        for row in grid:
            prvRow, curRow, prvCel = curRow, [0] * n, 0
            
            for idx, p in enumerate(prvRow):
                if row[idx] == 0:
                    curRow[idx], prvCel = prvCel + p, prvCel + p
                else:
                    curRow[idx], prvCel = prvCel, p

        return curRow[-1] %1_000_000_007
    
if __name__ == "__main__":
    solution = Solution()
    grid1 = [[0,1,0],[0,0,1],[1,0,0]]
    print(solution.uniquePaths(grid1))  # Output: 5

    grid2 = [[0,0],[0,0]]
    print(solution.uniquePaths(grid2))  # Output: 2

    grid3 = [[0,1,1],[1,1,0]]
    print(solution.uniquePaths(grid3))  # Output: 1