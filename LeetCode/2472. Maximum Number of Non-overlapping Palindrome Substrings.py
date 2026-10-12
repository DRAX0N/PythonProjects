"""
2472. Maximum Number of Non-overlapping Palindrome Substrings
Hard
Topics
premium lock icon
Companies
Hint
You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.

Example 2:

Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.
 

Constraints:

1 <= k <= s.length <= 2000
s consists of lowercase English letters.
"""

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # palindrome[i][j] == True if s[i:j + 1] is a palindrome
        palindrome = [[False] * n for _ in range(n)]

        # Length 1 substrings are always palindromes
        for i in range(n):
            palindrome[i][i] = True

        # Build the table by increasing substring length
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                if s[left] == s[right]:
                    if length <= 2 or palindrome[left + 1][right - 1]:
                        palindrome[left][right] = True

        # dp[i] = maximum number of valid non-overlapping palindromes
        # that can be selected from s[i:]
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            # Skip s[i]
            dp[i] = dp[i + 1]

            # Try every palindrome starting at i
            for right in range(i + k - 1, n):
                if palindrome[i][right]:
                    dp[i] = max(dp[i], 1 + dp[right + 1])

        return dp[0]
    
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        def check(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        n = len(s)
        ans = 0
        start = 0

        for r in range(k - 1, n):
            l = r - k + 1

            if l >= start and check(l, r):
                ans += 1
                start = r + 1
                continue
            
            l = r - k
            if l >= start and check(l, r):
                ans += 1
                start = r + 1

        return ans
    
if __name__ == "__main__":
    s = "abaccdbbd"
    k = 3
    solution = Solution()
    result = solution.maxPalindromes(s, k)
    print(result)  # Output: 2

    s = "adbcda"
    k = 2
    result = solution.maxPalindromes(s, k)
    print(result)  # Output: 0