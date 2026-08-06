"""
3518. Smallest Palindromic Rearrangement II
Hard
Topics
premium lock icon
Companies
Hint
You are given a palindromic string s and an integer k.

Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.

Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.

 

Example 1:

Input: s = "abba", k = 2

Output: "baab"

Explanation:

The two distinct palindromic rearrangements of "abba" are "abba" and "baab".
Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".
Example 2:

Input: s = "aa", k = 2

Output: ""

Explanation:

There is only one palindromic rearrangement: "aa".
The output is an empty string since k = 2 exceeds the number of possible rearrangements.
Example 3:

Input: s = "bacab", k = 1

Output: "abcba"

Explanation:

The two distinct palindromic rearrangements of "bacab" are "abcba" and "bacab".
Lexicographically, "abcba" comes before "bacab". Since k = 1, the output is "abcba".
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
s is guaranteed to be palindromic.
1 <= k <= 106
"""

from collections import Counter
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        odd = [ch for ch, c in cnt.items() if c % 2 == 1]
        if len(odd) > 1:
            return ""

        mid = odd[0] if odd else ""
        half = [0] * 26
        for ch, c in cnt.items():
            half[ord(ch) - 97] = c // 2

        total = self._count_perms(half)
        if k > total:
            return ""

        left = []
        half_len = sum(half)

        for _ in range(half_len):
            for i in range(26):
                if half[i] == 0:
                    continue
                half[i] -= 1
                ways = self._count_perms(half)
                if ways >= k:
                    left.append(chr(i + 97))
                    break
                k -= ways
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]

    def _count_perms(self, half):
        total = sum(half)
        res = 1
        for c in half:
            if c:
                res *= math.comb(total, c)
                if res > 10**6:
                    return 10**6 + 1
                total -= c
        return res

class Solution:
    def smallestPalindrome(self, S: str, K: int) -> str:
        import collections, math
        n = len(S)
        ans = [""] * n
        count = collections.Counter(S[: n // 2])
        if n & 1:
            ans[n // 2] = S[n // 2]
        tot = 0
        ways = 1
        i = 0
        for c in sorted(count, reverse=True):
            tot += count[c]
            ways *= math.comb(tot, count[c])
            if ways > K:
                for c2 in sorted(count):
                    if c2 >= c:
                        break
                    for loops in range(count[c2]):
                        ans[i] = ans[~i] = c2
                        i += 1
                    count[c2] = 0
        ways = 1
        tot = sum(count.values())
        for k in sorted(count):
            ways *= math.comb(tot, count[k])
            tot -= count[k]
        if ways < K:
            return ""
        tot = sum(count.values())
        while tot:
            for c in sorted(count):
                if count[c]:
                    ways2 = ways * count[c] // tot
                    if ways2 < K:
                        K -= ways2
                    else:
                        ans[i] = ans[~i] = c
                        i += 1
                        ways = ways2
                        count[c] -= 1
                        tot -= 1
                        break
        return "".join(ans)

if __name__ == "__main__":
    s = Solution()
    s1 = "abba"
    k1 = 2
    print(s.smallestPalindrome(s1, k1)) # Output: "baab"

    s2 = "aa"
    k2 = 2
    print(s.smallestPalindrome(s2, k2)) # Output: ""

    s3 = "bacab"
    k3 = 1
    print(s.smallestPalindrome(s3, k3)) # Output: "abcba"