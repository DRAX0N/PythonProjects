"""

Code
Testcase
Testcase
Test Result
1140. Stone Game II
Medium
Topics
premium lock icon
Companies
Hint
Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 

Example 1:

Input: piles = [2,7,9,4,4]

Output: 10

Explanation:

If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 stones in total.
If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 stones in total.
So we return 10 since it's larger.

Example 2:

Input: piles = [1,2,3,4,5,100]

Output: 104

 

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 104
"""

from functools import cache
from itertools import accumulate
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = list(accumulate(piles[::-1]))[::-1]

        @cache
        def dfs(i: int, m: int) -> int:
            # The current player can take all remaining piles.
            if i + 2 * m >= n:
                return suffix[i]

            # Try taking x piles, then let the opponent play optimally.
            best = 0

            for x in range(1, 2 * m + 1):
                opponent = dfs(i + x, max(m, x))
                current_player = suffix[i] - opponent
                best = max(best, current_player)

            return best

        return dfs(0, 1)
    
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0]*(n+1)

        for i in range(n-1,-1,-1):
            suffix[i] = piles[i] + suffix[i+1]
        
        @cache
        def dp(i,M):
            if (i+(2*M)) >= n:
                return suffix[i]
            best = 0
            for X in range(1,min(2*M,n-i)+1):
                opponent_score = dp(i+X,max(M,X))
                your_score = suffix[i] - opponent_score
                best = max(best, your_score)
            return best

        return dp(0,1)
    
if __name__ == "__main__":
    s = Solution()
    print(s.stoneGameII([2,7,9,4,4]))  # Output: 10
    print(s.stoneGameII([1,2,3,4,5,100]))  # Output: 104