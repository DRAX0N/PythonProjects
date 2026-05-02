"""
3225. Maximum Score From Grid Operations
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D matrix grid of size n x n. Initially, all cells of the grid are colored white. In one operation, you can select any cell of indices (i, j), and color black all the cells of the jth column starting from the top row down to the ith row.

The grid score is the sum of all grid[i][j] such that cell (i, j) is white and it has a horizontally adjacent black cell.

Return the maximum score that can be achieved after some number of operations.

 

Example 1:

Input: grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]

Output: 11

Explanation:


In the first operation, we color all cells in column 1 down to row 3, and in the second operation, we color all cells in column 4 down to the last row. The score of the resulting grid is grid[3][0] + grid[1][2] + grid[3][3] which is equal to 11.

Example 2:

Input: grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]

Output: 94

Explanation:


We perform operations on 1, 2, and 3 down to rows 1, 4, and 0, respectively. The score of the resulting grid is grid[0][0] + grid[1][0] + grid[2][1] + grid[4][1] + grid[1][3] + grid[2][3] + grid[3][3] + grid[4][3] + grid[0][4] which is equal to 94.

 

Constraints:

1 <= n == grid.length <= 100
n == grid[i].length
0 <= grid[i][j] <= 109
"""
from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0

        # prefix sum per column
        col_sum = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for r in range(1, n + 1):
                col_sum[c][r] = col_sum[c][r - 1] + grid[r - 1][c]

        INF = float('-inf')
        # dp[currH][prevH] - rolling array (only previous column needed)
        dp = [[INF] * (n + 1) for _ in range(n + 1)]
        prev_max = [[INF] * (n + 1) for _ in range(n + 1)]
        prev_suffix_max = [[INF] * (n + 1) for _ in range(n + 1)]

        # initialize first column (i=0): no score yet, any height possible
        for h in range(n + 1):
            dp[h][0] = 0  # prev col doesn't exist, prevH=0 conceptually

        # Rebuild prevMax and prevSuffixMax for i=0
        for curr_h in range(n + 1):
            prev_max[curr_h][0] = dp[curr_h][0]
            for prev_h in range(1, n + 1):
                penalty = col_sum[0][prev_h] - col_sum[0][curr_h] if prev_h > curr_h else 0
                prev_max[curr_h][prev_h] = max(
                    prev_max[curr_h][prev_h - 1],
                    dp[curr_h][prev_h] - penalty
                )
            prev_suffix_max[curr_h][n] = dp[curr_h][n]
            for prev_h in range(n - 1, -1, -1):
                prev_suffix_max[curr_h][prev_h] = max(
                    prev_suffix_max[curr_h][prev_h + 1],
                    dp[curr_h][prev_h]
                )

        for i in range(1, n):
            new_dp = [[INF] * (n + 1) for _ in range(n + 1)]
            for curr_h in range(n + 1):
                for prev_h in range(n + 1):
                    if curr_h <= prev_h:
                        extra = col_sum[i][prev_h] - col_sum[i][curr_h]
                        val = prev_suffix_max[prev_h][0]
                        if val != INF:
                            new_dp[curr_h][prev_h] = val + extra
                    else:
                        extra = col_sum[i - 1][curr_h] - col_sum[i - 1][prev_h]
                        a = prev_suffix_max[prev_h][curr_h]
                        b = prev_max[prev_h][curr_h]
                        best = INF
                        if a != INF:
                            best = max(best, a)
                        if b != INF:
                            best = max(best, b + extra)
                        new_dp[curr_h][prev_h] = best

            # update helpers
            for curr_h in range(n + 1):
                prev_max[curr_h][0] = new_dp[curr_h][0]
                for prev_h in range(1, n + 1):
                    penalty = col_sum[i][prev_h] - col_sum[i][curr_h] if prev_h > curr_h else 0
                    v = new_dp[curr_h][prev_h]
                    prev_max[curr_h][prev_h] = max(
                        prev_max[curr_h][prev_h - 1],
                        (v - penalty) if v != INF else INF
                    )
                prev_suffix_max[curr_h][n] = new_dp[curr_h][n]
                for prev_h in range(n - 1, -1, -1):
                    prev_suffix_max[curr_h][prev_h] = max(
                        prev_suffix_max[curr_h][prev_h + 1],
                        new_dp[curr_h][prev_h]
                    )
            dp = new_dp

        ans = 0
        for k in range(n + 1):
            for h in [0, n]:
                if dp[h][k] != INF:
                    ans = max(ans, dp[h][k])
        return ans
    
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        prev_col_w = [0] * (n+1) # [DP] prev col with prev col's score
        prev_col_wo = [0] * (n+1) # [DP] prev col without prev col's score
        if n == 1:
            return 0

        for j in range(1, n): # [LOOP] for each col
            cur_col_w = [0] * (n+1) # [DP] cur col with cur col's score
            cur_col_wo = [0] * (n+1) # [DP] cur col without cur col's score
            for i in range(n+1): # [LOOP] prev col (j-1) is black from row 0 to row i-1 (no black when i == 0)
                prev_col_val = 0 # prev col (j-1) score when prev black is i and cur black is k
                cur_col_val = 0 # cur col (j) score when prev black is i and cur black is k
                for p in range(i):
                    cur_col_val += grid[p][j]
                for k in range(n+1): # [LOOP] cur col (j) black is from row 0 to row k-1 (no black when k == 0)
                    if k > 0 and k <= i:
                        cur_col_val -= grid[k-1][j]
                    if k > i:
                        prev_col_val += grid[k-1][j-1]
                    cur_col_wo[k] = max(cur_col_wo[k], prev_col_val + prev_col_wo[i])
                    cur_col_wo[k] = max(cur_col_wo[k], prev_col_w[i])
                    cur_col_w[k] = max(cur_col_w[k], cur_col_val + prev_col_w[i])
                    cur_col_w[k] = max(cur_col_w[k], cur_col_val + prev_col_val + prev_col_wo[i])
            prev_col_w = cur_col_w
            prev_col_wo = cur_col_wo
        return max(cur_col_w)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumScore([[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]])) #11
    print(solution.maximumScore([[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]])) #94