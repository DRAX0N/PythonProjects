"""
115. Distinct Subsequences
Hard
Topics
premium lock icon
Companies
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # Create a 2D DP array with (m+1) x (n+1) dimensions
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # An empty string t can be formed from any prefix of s in exactly one way
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # If characters match, we can either use this character or skip it
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # If characters don't match, we can only skip the character from s
                    dp[i][j] = dp[i - 1][j]
        
        return dp[m][n]

if __name__ == "__main__":
    s = "rabbbit"
    t = "rabbit"
    solution = Solution()
    result = solution.numDistinct(s, t)
    print(result)  # Output: 3

    s = "babgbag"
    t = "bag"
    result = solution.numDistinct(s, t)
    print(result)  # Output: 5