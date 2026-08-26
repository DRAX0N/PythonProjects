"""
1563. Stone Game V
Attempted
Hard
Topics
premium lock icon
Companies
Hint
There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's score is initially zero.

Return the maximum score that Alice can obtain.

 

Example 1:

Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
Example 2:

Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28
Example 3:

Input: stoneValue = [4]
Output: 0
 

Constraints:

1 <= stoneValue.length <= 500
1 <= stoneValue[i] <= 106
"""

from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        # prefix[i] = sum of stoneValue[0..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
        
        # dp[i][j] = max score Alice can get from stoneValue[i..j]
        dp = [[0] * n for _ in range(n)]
        
        # length = subarray size
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                best = 0
                for k in range(i, j):
                    left_sum = prefix[k + 1] - prefix[i]
                    right_sum = prefix[j + 1] - prefix[k + 1]
                    
                    if left_sum < right_sum:
                        best = max(best, left_sum + dp[i][k])
                    elif left_sum > right_sum:
                        best = max(best, right_sum + dp[k + 1][j])
                    else:
                        best = max(best, left_sum + max(dp[i][k], dp[k + 1][j]))
                
                dp[i][j] = best
        
        return dp[0][n - 1]
    
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        left_best = [[0] * n for _ in range(n)]

        right_best = [[0] * n for _ in range(n)]

        left_ptr = [0] * n

        right_ptr = list(range(n))

        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

            left_ptr[i] = i - 1

            right_ptr[i] = i

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                total = prefix[r + 1] - prefix[l]

                while left_ptr[l] + 1 <= r - 1:
                    k = left_ptr[l] + 1
                    left_sum = prefix[k + 1] - prefix[l]

                    if 2 * left_sum > total:
                        break

                    left_ptr[l] += 1

                while right_ptr[l] <= r - 1:
                    k = right_ptr[l]
                    left_sum = prefix[k + 1] - prefix[l]

                    if 2 * left_sum >= total:
                        break

                    right_ptr[l] += 1

                best = 0

                if left_ptr[l] >= l:
                    best = left_best[l][left_ptr[l]]

                if right_ptr[l] <= r - 1:
                    best = max(
                        best,
                        right_best[right_ptr[l] + 1][r]
                    )

                dp[l][r] = best

                left_best[l][r] = max(
                    left_best[l][r - 1],
                    dp[l][r] + total
                )

                right_best[l][r] = max(
                    right_best[l + 1][r],
                    dp[l][r] + total
                )

        return dp[0][n - 1]
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.stoneGameV([6,2,3,4,5,5]))  # Output: 18
    print(solution.stoneGameV([7,7,7,7,7,7,7]))  # Output: 28
    print(solution.stoneGameV([4]))  # Output: 0