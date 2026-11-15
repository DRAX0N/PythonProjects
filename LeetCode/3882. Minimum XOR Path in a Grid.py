"""
3882. Minimum XOR Path in a Grid
Medium
Topics
premium lock icon
Companies
Hint
You are given a 2D integer array grid of size m * n.

You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).

At each step, you may move either right or down.

The cost of a path is defined as the bitwise XOR of all the values in the cells along that path, including the start and end cells.

Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).

 

Example 1:

Input: grid = [[1,2],[3,4]]

Output: 6

Explanation:

There are two valid paths:

(0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
(0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6
The minimum XOR value among all valid paths is 6.

Example 2:

Input: grid = [[6,7],[5,8]]

Output: 9

Explanation:

There are two valid paths:

(0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
(0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11
The minimum XOR value among all valid paths is 9.

Example 3:

Input: grid = [[2,7,5]]

Output: 0

Explanation:

There is only one valid path:

(0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0
The XOR value of this path is 0, which is the minimum possible.

 

Constraints:

1 <= m == grid.length <= 1000
1 <= n == grid[i].length <= 1000
m * n <= 1000
0 <= grid[i][j] <= 1023​
"""

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # dp[i][j] = zbiór wszystkich możliwych XOR-ów ścieżek kończących się w (i, j)
        dp = [[set() for _ in range(cols)] for _ in range(rows)]
        dp[0][0].add(grid[0][0])

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue

                current = set()

                if i > 0:
                    for value in dp[i - 1][j]:
                        current.add(value ^ grid[i][j])

                if j > 0:
                    for value in dp[i][j - 1]:
                        current.add(value ^ grid[i][j])

                dp[i][j] = current

        return min(dp[rows - 1][cols - 1])

if __name__ == "__main__":
    solution = Solution()
    grid1 = [[1, 2], [3, 4]]
    print(solution.minCost(grid1))  # Output: 6

    grid2 = [[6, 7], [5, 8]]
    print(solution.minCost(grid2))  # Output: 9

    grid3 = [[2, 7, 5]]
    print(solution.minCost(grid3))  # Output: 0