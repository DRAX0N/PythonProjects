"""
1391. Check if There is a Valid Path in a Grid
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.

You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

 

Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
"""
from collections import deque
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        street_dirs = {
            1: [('L', (0,-1)), ('R', (0,1))],
            2: [('U', (-1,0)), ('D', (1,0))],
            3: [('L', (0,-1)), ('D', (1,0))],
            4: [('R', (0,1)),  ('D', (1,0))],
            5: [('L', (0,-1)), ('U', (-1,0))],
            6: [('R', (0,1)),  ('U', (-1,0))],
        }
        accepts = {
            'R': {1, 3, 5},
            'L': {1, 4, 6},
            'D': {2, 5, 6},
            'U': {2, 3, 4},
        }

        visited = [[False] * n for _ in range(m)]
        queue = deque([(0, 0)])
        visited[0][0] = True

        while queue:
            r, c = queue.popleft()

            if r == m - 1 and c == n - 1:
                return True

            for direction, (dr, dc) in street_dirs[grid[r][c]]:
                nr, nc = r + dr, c + dc
                # sprawdź granicę, odwiedziny i kompatybilność sąsiada
                if 0 <= nr < m and 0 <= nc < n \
                   and not visited[nr][nc] \
                   and grid[nr][nc] in accepts[direction]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.hasValidPath([[2,4,3],[6,5,2]]))  # True
    print(s.hasValidPath([[1,2,1],[1,2,1]]))  # False
    print(s.hasValidPath([[1,1,2]]))          # False