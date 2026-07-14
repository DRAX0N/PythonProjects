"""
3286. Find a Safe Walk Through a Grid
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n binary matrix grid and an integer health.

You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).

You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

 

Example 1:

Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.


Example 2:

Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3

Output: false

Explanation:

A minimum of 4 health points is needed to reach the final cell safely.


Example 3:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.



Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.
"""
from typing import List
from collections import deque
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        d=(0, 1, 0, -1, 0)
        r, c=len(grid), len(grid[0])
        N=r*c
        def idx(i, j):
            return i*c+j
        maxH=[-1]*N
        q=deque()
        q.append(0)
        maxH[0]=health-grid[0][0]
        while q:
            ij=q.popleft()
            curH=maxH[ij]
            if ij==N-1:
                return curH>0
            i, j=divmod(ij, c)
            for a in range(4):
                s, t=i+d[a], j+d[a+1]
                st=idx(s, t)
                if s<0 or s>=r or t<0 or t>=c:
                    continue
                H2=curH-grid[s][t]
                if H2>maxH[st]:
                    maxH[st]=H2
                    if grid[s][t]==0:
                        q.appendleft(st)
                    else:
                        q.append(st)
        return False

if __name__ == "__main__":
    print(Solution().findSafeWalk([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], 1)) #True
    print(Solution().findSafeWalk([[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], 3)) #False
    print(Solution().findSafeWalk([[1,1,1],[1,0,1],[1,1,1]], 5)) #True