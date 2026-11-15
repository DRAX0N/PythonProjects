"""
3619. Count Islands With Total Value Divisible by K
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).

The total value of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value divisible by k.

 

Example 1:


Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5

Output: 2

Explanation:

The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

Example 2:


Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3

Output: 6

Explanation:

The grid contains six islands, each with a total value that is divisible by 3.

 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
0 <= grid[i][j] <= 106
1 <= k <= 106
"""
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            value = grid[r][c]
            grid[r][c] = 0  # Mark the cell as visited
            value += dfs(r - 1, c)
            value += dfs(r + 1, c)
            value += dfs(r, c - 1)
            value += dfs(r, c + 1)
            return value

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    total_value = dfs(r, c)
                    if total_value % k == 0:
                        count += 1

        return count

if __name__ == "__main__":
    solution = Solution()
    grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]]
    k = 5
    print(solution.countIslands(grid, k))  # Output: 2

    grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]]
    k = 3
    print(solution.countIslands(grid, k))  # Output: 6