"""
3568. Minimum Moves to Clean the Classroom
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

'S': Starting position of the student
'L': Litter that must be collected (once collected, the cell becomes empty)
'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
'X': Obstacle the student cannot pass through
'.': Empty space
You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.

Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.

 

Example 1:

Input: classroom = ["S.", "XL"], energy = 2

Output: 2

Explanation:

The student starts at cell (0, 0) with 2 units of energy.
Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.
A valid sequence of moves to collect all litter is as follows:
Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.
Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.
The student collects all the litter using 2 moves. Thus, the output is 2.
Example 2:

Input: classroom = ["LS", "RL"], energy = 4

Output: 3

Explanation:

The student starts at cell (0, 1) with 4 units of energy.
A valid sequence of moves to collect all litter is as follows:
Move 1: From (0, 1) → (0, 0) to collect the first litter 'L' with 1 unit of energy used and 3 units remaining.
Move 2: From (0, 0) → (1, 0) to 'R' to reset and restore energy back to 4.
Move 3: From (1, 0) → (1, 1) to collect the second litter 'L'.
The student collects all the litter using 3 moves. Thus, the output is 3.
Example 3:

Input: classroom = ["L.S", "RXL"], energy = 3

Output: -1

Explanation:

No valid path collects all 'L'.

 

Constraints:

1 <= m == classroom.length <= 20
1 <= n == classroom[i].length <= 20
classroom[i][j] is one of 'S', 'L', 'R', 'X', or '.'
1 <= energy <= 50
There is exactly one 'S' in the grid.
There are at most 10 'L' cells in the grid.
"""

from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        # Map each 'L' to an index 0..k-1
        litter_id = [[-1] * n for _ in range(m)]
        start_r = start_c = 0
        k = 0
        
        for i in range(m):
            for j, ch in enumerate(classroom[i]):
                if ch == 'S':
                    start_r, start_c = i, j
                elif ch == 'L':
                    litter_id[i][j] = k
                    k += 1
        
        # No litter to collect
        if k == 0:
            return 0
        
        # vis[r][c][e][mask]
        vis = [
            [
                [[False] * (1 << k) for _ in range(energy + 1)]
                for _ in range(n)
            ]
            for _ in range(m)
        ]
        
        initial_mask = (1 << k) - 1  # all litter uncollected
        q = [(start_r, start_c, energy, initial_mask)]
        vis[start_r][start_c][energy][initial_mask] = True
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        moves = 0
        
        while q:
            nxt = []
            for r, c, e, mask in q:
                if mask == 0:
                    return moves
                if e <= 0:
                    continue
                
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    cell = classroom[nr][nc]
                    if cell == 'X':
                        continue
                    
                    # New energy
                    if cell == 'R':
                        ne = energy
                    else:
                        ne = e - 1
                    
                    # New mask
                    nmask = mask
                    if cell == 'L':
                        idx = litter_id[nr][nc]
                        nmask = mask & ~(1 << idx)
                    
                    if not vis[nr][nc][ne][nmask]:
                        vis[nr][nc][ne][nmask] = True
                        nxt.append((nr, nc, ne, nmask))
            
            q = nxt
            moves += 1
        
        return -1
        
if __name__ == "__main__":
    solution = Solution()
    classroom = ["S.", "XL"]
    energy = 2
    print(solution.minMoves(classroom, energy))  # Output: 2

    classroom = ["LS", "RL"]
    energy = 4
    print(solution.minMoves(classroom, energy))  # Output: 3

    classroom = ["L.S", "RXL"]
    energy = 3
    print(solution.minMoves(classroom, energy))  # Output: -1

    classroom = ["S.", "XL"]
    energy = 2
    print(solution.minMoves(classroom, energy))  # Output: 2