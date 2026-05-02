"""

Code


Testcase
Testcase
Test Result
3418. Maximum Amount of Money Robot Can Earn
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n grid. A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). The robot can move either right or down at any point in time.

The grid contains a value coins[i][j] in each cell:

If coins[i][j] >= 0, the robot gains that many coins.
If coins[i][j] < 0, the robot encounters a robber, and the robber steals the absolute value of coins[i][j] coins.
The robot has a special ability to neutralize robbers in at most 2 cells on its path, preventing them from stealing coins in those cells.

Note: The robot's total coins can be negative.

Return the maximum profit the robot can gain on the route.

 

Example 1:

Input: coins = [[0,1,-1],[1,-2,3],[2,-3,4]]

Output: 8

Explanation:

An optimal path for maximum coins is:

Start at (0, 0) with 0 coins (total coins = 0).
Move to (0, 1), gaining 1 coin (total coins = 0 + 1 = 1).
Move to (1, 1), where there's a robber stealing 2 coins. The robot uses one neutralization here, avoiding the robbery (total coins = 1).
Move to (1, 2), gaining 3 coins (total coins = 1 + 3 = 4).
Move to (2, 2), gaining 4 coins (total coins = 4 + 4 = 8).
Example 2:

Input: coins = [[10,10,10],[10,10,10]]

Output: 40

Explanation:

An optimal path for maximum coins is:

Start at (0, 0) with 10 coins (total coins = 10).
Move to (0, 1), gaining 10 coins (total coins = 10 + 10 = 20).
Move to (0, 2), gaining another 10 coins (total coins = 20 + 10 = 30).
Move to (1, 2), gaining the final 10 coins (total coins = 30 + 10 = 40).
 

Constraints:

m == coins.length
n == coins[i].length
1 <= m, n <= 500
-1000 <= coins[i][j] <= 1000
"""

from cmath import inf
from typing import List


#class Solution:
#    def maximumAmount(self, coins: List[List[int]]) -> int:     
#        # count amount of coins at the end of road from top left to bottom right - step can go only right or down
#        # you can decline adding coins from 2 cells with negative value (robbers)
#        all_routs = []
#        m, n = len(coins), len(coins[0])
#        
#        def dfs(i, j, amount, robbed):
#            if i == m - 1 and j == n - 1:
#                all_routs.append(amount)
#                return
#            if i < m - 1:
#                if coins[i + 1][j] < 0 and robbed < 2:
#                    dfs(i + 1, j, amount, robbed + 1)
#                dfs(i + 1, j, amount + coins[i + 1][j], robbed)
#            if j < n - 1:
#                if coins[i][j + 1] < 0 and robbed < 2:
#                    dfs(i, j + 1, amount, robbed + 1)
#                dfs(i, j + 1, amount + coins[i][j + 1], robbed)
#        if coins[0][0] < 0:
#            dfs(0, 0, 0, 1)
#        dfs(0, 0, coins[0][0], 0)
#        
#        return max(all_routs)
    
#class Solution:
#    def maximumAmount(self, coins: List[List[int]]) -> int:
#        m, n = len(coins), len(coins[0])
#        # dp[i][j][k] = max suma do (i,j) używając k rabusiów (0,1,2)
#        dp = [[[float('-inf')] * 3 for _ in range(n)] for _ in range(m)]
#        
#        # Start
#        if coins[0][0] < 0:
#            dp[0][0][0] = coins[0][0]
#            dp[0][0][1] = 0
#        else:
#            dp[0][0][0] = coins[0][0]
#        
#        # Wypełnij DP
#        for i in range(m):
#            for j in range(n):
#                if i == 0 and j == 0:
#                    continue
#                    
#                curr = coins[i][j]
#                is_negative = curr < 0
#                
#                # Z góry
#                if i > 0:
#                    for prev_robbed in range(3):
#                        prev_value = dp[i-1][j][prev_robbed]
#                        if prev_value == float('-inf'):
#                            continue
#                        if is_negative:
#                            # use neutralization if available
#                            if prev_robbed < 2:
#                                dp[i][j][prev_robbed + 1] = max(dp[i][j][prev_robbed + 1], prev_value)
#                            # do not use neutralization
#                            dp[i][j][prev_robbed] = max(dp[i][j][prev_robbed], prev_value + curr)
#                        else:
#                            dp[i][j][prev_robbed] = max(dp[i][j][prev_robbed], prev_value + curr)
#                
#                # Z lewej
#                if j > 0:
#                    for prev_robbed in range(3):
#                        prev_value = dp[i][j-1][prev_robbed]
#                        if prev_value == float('-inf'):
#                            continue
#                        if is_negative:
#                            if prev_robbed < 2:
#                                dp[i][j][prev_robbed + 1] = max(dp[i][j][prev_robbed + 1], prev_value)
#                            dp[i][j][prev_robbed] = max(dp[i][j][prev_robbed], prev_value + curr)
#                        else:
#                            dp[i][j][prev_robbed] = max(dp[i][j][prev_robbed], prev_value + curr)
#        
#        # Wynik
#        print(dp)
#        return max(dp[m-1][n-1])
    
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])

        dp = [[-inf] * 3 for _ in range(n+1)]
        # initialise the first row
        dp[1] = [0] * 3

        for i in range(m):
            for j in range(n):
                x = coins[i][j]
                up0, up1, up2 = dp[j+1]
                left0, left1, left2 = dp[j]
                dp[j+1][0] = max(up0, left0) + x
                dp[j+1][1] = max(up1+x, left1+x, up0, left0) 
                dp[j+1][2] = max(up2+x, left2+x, up1, left1) 
        return dp[n][2]
    
if __name__ == "__main__":
    s = Solution()
    print(s.maximumAmount([[0,1,-1],[1,-2,3],[2,-3,4]]))  # Output: 8
    print(s.maximumAmount([[10,10,10],[10,10,10]]))  # Output: 40
    print(s.maximumAmount([[-4]])) # Output: 0
    print(s.maximumAmount([[-7,12,12,13],[-6,19,19,-6],[9,-2,-10,16],[-4,14,-10,-9]])) # Output: 60