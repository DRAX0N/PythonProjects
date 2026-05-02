"""
3212. Count Submatrices With Equal Frequency of X and Y
Medium
Topics
premium lock icon
Companies
Hint
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.
 

Example 1:

Input: grid = [["X","Y","."],["Y",".","."]]

Output: 3

Explanation:



Example 2:

Input: grid = [["X","X"],["X","Y"]]

Output: 0

Explanation:

No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:

Input: grid = [[".","."],[".","."]]

Output: 0

Explanation:

No submatrix has at least one 'X'.

 

Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 'X', 'Y', or '.'.
"""

from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        # px[i][j] = liczba 'X' w prostokącie (0,0)..(i,j)
        px = [[0] * n for _ in range(m)]
        py = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                px[i][j] = (1 if grid[i][j] == 'X' else 0)
                py[i][j] = (1 if grid[i][j] == 'Y' else 0)
                if i > 0:
                    px[i][j] += px[i-1][j]
                    py[i][j] += py[i-1][j]
                if j > 0:
                    px[i][j] += px[i][j-1]
                    py[i][j] += py[i][j-1]
                if i > 0 and j > 0:
                    px[i][j] -= px[i-1][j-1]
                    py[i][j] -= py[i-1][j-1]

                # Submatryca (0,0)..(i,j) — prefix to gotowa odpowiedź
                if px[i][j] > 0 and px[i][j] == py[i][j]:
                    count += 1

        return count



class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        arr = [0 for _ in range(n)]
        arr1 = [0 for _ in range(n)]
        ans = 0
        for i in range(m):
            pre, pre1 = 0, 0
            for j in range(n):
                if grid[i][j] == '.':
                    arr[j] += 0
                elif grid[i][j] == 'X':
                    arr[j] += 1
                    arr1[j] += 1
                else:
                    arr[j] -= 1
                pre += arr[j]
                pre1 += arr1[j]
                if pre == 0 and pre1 > 0:
                    ans += 1
        return ans   
if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSubmatrices([["X","Y","."],["Y",".","."]]))  # Output: 3
    print(s.numberOfSubmatrices([["X","X"],["X","Y"]]))  # Output: 0
    print(s.numberOfSubmatrices([[".","."],[".","."]]))  # Output: 0