"""
2911. Minimum Changes to Make K Semi-palindromes
Hard
Topics
premium lock icon
Companies
Hint
Given a string s and an integer k, partition s into k substrings such that the letter changes needed to make each substring a semi-palindrome are minimized.

Return the minimum number of letter changes required.

A semi-palindrome is a special type of string that can be divided into palindromes based on a repeating pattern. To check if a string is a semi-palindrome:​

Choose a positive divisor d of the string's length. d can range from 1 up to, but not including, the string's length. For a string of length 1, it does not have a valid divisor as per this definition, since the only divisor is its length, which is not allowed.
For a given divisor d, divide the string into groups where each group contains characters from the string that follow a repeating pattern of length d. Specifically, the first group consists of characters at positions 1, 1 + d, 1 + 2d, and so on; the second group includes characters at positions 2, 2 + d, 2 + 2d, etc.
The string is considered a semi-palindrome if each of these groups forms a palindrome.
Consider the string "abcabc":

The length of "abcabc" is 6. Valid divisors are 1, 2, and 3.
For d = 1: The entire string "abcabc" forms one group. Not a palindrome.
For d = 2:
Group 1 (positions 1, 3, 5): "acb"
Group 2 (positions 2, 4, 6): "bac"
Neither group forms a palindrome.
For d = 3:
Group 1 (positions 1, 4): "aa"
Group 2 (positions 2, 5): "bb"
Group 3 (positions 3, 6): "cc"
All groups form palindromes. Therefore, "abcabc" is a semi-palindrome.
 

Example 1:

Input: s = "abcac", k = 2

Output: 1

Explanation: Divide s into "ab" and "cac". "cac" is already semi-palindrome. Change "ab" to "aa", it becomes semi-palindrome with d = 1.

Example 2:

Input: s = "abcdef", k = 2

Output: 2

Explanation: Divide s into substrings "abc" and "def". Each needs one change to become semi-palindrome.

Example 3:

Input: s = "aabbaa", k = 3

Output: 0

Explanation: Divide s into substrings "aa", "bb" and "aa". All are already semi-palindromes.

 

Constraints:

2 <= s.length <= 200
1 <= k <= s.length / 2
s contains only lowercase English letters.
"""

from math import inf

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        divs = [[] for _ in range(n + 1)]
        for L in range(2, n + 1):
            divs[L] = [d for d in range(1, L) if L % d == 0]

        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                best = inf
                for d in divs[L]:
                    c = 0
                    for r in range(d):
                        lo, hi = i + r, i + r + ((L // d) - 1) * d
                        while lo < hi:
                            if s[lo] != s[hi]:
                                c += 1
                            lo += d
                            hi -= d
                    best = min(best, c)
                cost[i][j] = best  # len 1 niedozwolone -> inf poniżej

        for i in range(n):
            cost[i][i] = inf  # pojedyncza litera nie jest semi-palindromem

        dp = [[inf] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for i in range(p * 2, n + 1):
                for j in range((p - 1) * 2, i - 1):
                    v = dp[p - 1][j] + cost[j][i - 1]
                    if v < dp[p][i]:
                        dp[p][i] = v
        return dp[k][n]

if __name__ == "__main__":
    s = "abcac"
    k = 2
    solution = Solution()
    result = solution.minimumChanges(s, k)
    print(result)  # Output: 1

    s = "abcdef"
    k = 2
    result = solution.minimumChanges(s, k)
    print(result)  # Output: 2

    s = "aabbaa"
    k = 3
    result = solution.minimumChanges(s, k)
    print(result)  # Output: 0