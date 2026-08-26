"""
3090. Maximum Length Substring With Two Occurrences
Easy
Topics
premium lock icon
Companies
Hint
Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
"""
from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = l = 0
        fq = defaultdict(int)

        for r, ch in enumerate(s):
            fq[ch] += 1
            while fq[ch] > 2:
                fq[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)

        return res

        
        

if __name__ == "__main__":
    s = Solution()
    print(s.maximumLengthSubstring("bcbbbcba"))  # Output: 4
    print(s.maximumLengthSubstring("aaaa"))      # Output: 2
    print(s.maximumLengthSubstring("acedc"))      # Output: 5