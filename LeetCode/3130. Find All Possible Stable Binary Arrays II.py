"""
3130. Find All Possible Stable Binary Arrays II
Hard
Topics
premium lock icon
Companies
Hint
You are given 3 positive integers zero, one, and limit.

A binary array arr is called stable if:

The number of occurrences of 0 in arr is exactly zero.
The number of occurrences of 1 in arr is exactly one.
Each subarray of arr with a size greater than limit must contain both 0 and 1.
Return the total number of stable binary arrays.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: zero = 1, one = 1, limit = 2

Output: 2

Explanation:

The two possible stable binary arrays are [1,0] and [0,1].

Example 2:

Input: zero = 1, one = 2, limit = 1

Output: 1

Explanation:

The only possible stable binary array is [1,0,1].

Example 3:

Input: zero = 3, one = 3, limit = 2

Output: 14

Explanation:

All the possible stable binary arrays are [0,0,1,0,1,1], [0,0,1,1,0,1], [0,1,0,0,1,1], [0,1,0,1,0,1], [0,1,0,1,1,0], [0,1,1,0,0,1], [0,1,1,0,1,0], [1,0,0,1,0,1], [1,0,0,1,1,0], [1,0,1,0,0,1], [1,0,1,0,1,0], [1,0,1,1,0,0], [1,1,0,0,1,0], and [1,1,0,1,0,0].

 

Constraints:

1 <= zero, one, limit <= 1000
"""

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]
        #print(dp)
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1

        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
                if i - limit - 1 >= 0:
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1]) % MOD

                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD
                if j - limit - 1 >= 0:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0]) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
    
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        end0 = [[0] * (one + 1) for _ in range(zero + 1)]
        end1 = [[0] * (one + 1) for _ in range(zero + 1)]

        for i in range(1, min(zero, limit) + 1):
            end0[i][0] = 1

        for j in range(1, min(one, limit) + 1):
            end1[0][j] = 1

        for i in range(1, zero + 1):
            row0 = end0[i]
            row1 = end1[i]
            prev0 = end0[i - 1]
            prev1 = end1[i - 1]

            for j in range(1, one + 1):
                val0 = prev0[j] + prev1[j]
                if i - limit - 1 >= 0:
                    val0 -= end1[i - limit - 1][j]
                row0[j] = val0 % MOD

                val1 = row0[j - 1] + row1[j - 1]
                if j - limit - 1 >= 0:
                    val1 -= row0[j - limit - 1]
                row1[j] = val1 % MOD

        return (end0[zero][one] + end1[zero][one]) % MOD

    
if __name__ == "__main__":
    s = Solution()
    #print(s.numberOfStableArrays(1, 1, 2)) #2
    #print(s.numberOfStableArrays(1, 2, 1)) #1
    #print(s.numberOfStableArrays(3, 3, 2)) #14
#
    zero = 791
    one = 796
    limit = 331
    print(s.numberOfStableArrays(zero, one, limit)) # 381273302