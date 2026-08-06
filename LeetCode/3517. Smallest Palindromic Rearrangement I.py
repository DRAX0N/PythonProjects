"""
3517. Smallest Palindromic Rearrangement I
Medium
Topics
premium lock icon
Companies
Hint
You are given a palindromic string s.

Return the lexicographically smallest palindromic permutation of s.

 

Example 1:

Input: s = "z"

Output: "z"

Explanation:

A string of only one character is already the lexicographically smallest palindrome.

Example 2:

Input: s = "babab"

Output: "abbba"

Explanation:

Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.

Example 3:

Input: s = "daccad"

Output: "acddca"

Explanation:

Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.

 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
s is guaranteed to be palindromic.

"""

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        print("================")
        s_len = len(s)
        s_range = s_len//2
        m = ""    
        if s_len == 1:
            m = s
        elif s_len%2 == 1 and s_len>1:
            m = s[s_len//2]
        ch_dict = {}
        for i in range(s_range):
            if s[i] in ch_dict:
                ch_dict[s[i]] += 1
            else:
                ch_dict[s[i]] = 1

        characters = []
        for ch in ch_dict.keys():
            characters.append(ch)

        characters.sort()
        res = ""
        for ch in characters:
            res += ch_dict[ch]*ch
        res += m 
        for ch in characters[::-1]:
            res += ch_dict[ch]*ch
        return res
    
import numpy as np
from string import ascii_lowercase
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # counts = sorted(Counter(s).items())
        # half = "".join(c * (k // 2) for c, k in counts)
        # mid  = "".join(c * (k % 2)  for c, k in counts)
        # return half + mid + half[::-1]
        counts = np.bincount(np.frombuffer(s.encode(), np.uint8), minlength=123)[97:].tolist()
        half = "".join(c * (k // 2) for c, k in zip(ascii_lowercase, counts))
        mid  = "".join(c * (k % 2)  for c, k in zip(ascii_lowercase, counts))
        return half + mid + half[::-1]    
    
if __name__ == "__main__":
    s = Solution()
    ch = "z"
    print(s.smallestPalindrome(ch)) # z
    ch = "babab"
    print(s.smallestPalindrome(ch)) # abbba
    ch = "daccad"
    print(s.smallestPalindrome(ch)) # acddca