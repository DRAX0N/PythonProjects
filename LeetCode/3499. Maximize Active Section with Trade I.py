"""
3499. Maximize Active Section with Trade I
Medium
Topics
premium lock icon
Companies
Hint
You are given a binary string s of length n, where:

'1' represents an active section.
'0' represents an inactive section.
You can perform at most one trade to maximize the number of active sections in s. In a trade, you:

Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
Return the maximum number of active sections in s after making the optimal trade.

Note: Treat s as if it is augmented with a '1' at both ends, forming t = '1' + s + '1'. The augmented '1's do not contribute to the final count.

 

Example 1:

Input: s = "01"

Output: 1

Explanation:

Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

Example 2:

Input: s = "0100"

Output: 4

Explanation:

String "0100" → Augmented to "101001".
Choose "0100", convert "101001" → "100001" → "111111".
The final string without augmentation is "1111". The maximum number of active sections is 4.
Example 3:

Input: s = "1000100"

Output: 7

Explanation:

String "1000100" → Augmented to "110001001".
Choose "000100", convert "110001001" → "110000001" → "111111111".
The final string without augmentation is "1111111". The maximum number of active sections is 7.
Example 4:

Input: s = "01010"

Output: 4

Explanation:

String "01010" → Augmented to "1010101".
Choose "010", convert "1010101" → "1000101" → "1111101".
The final string without augmentation is "11110". The maximum number of active sections is 4.
 

Constraints:

1 <= n == s.length <= 105
s[i] is either '0' or '1'
"""

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')

        s = '1' + s + '1'

        n = len(s)
        i = 0

        ans = ones

        # Skip first 1's
        while i < n and s[i] == '1':
            i += 1

        # Read first 0-block
        c10 = 0
        while i < n and s[i] == '0':
            c10 += 1
            i += 1

        while i < n:

            # Read middle 1-block
            c11 = 0
            while i < n and s[i] == '1':
                c11 += 1
                i += 1

            if c11 == 0:
                break

            # Read right 0-block
            c20 = 0
            while i < n and s[i] == '0':
                c20 += 1
                i += 1

            if c20 == 0:
                break

            ans = max(ans, ones + c10 + c20)

            # Slide the window
            c10 = c20

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.maxActiveSectionsAfterTrade("01")) # 1
    print(s.maxActiveSectionsAfterTrade("0100")) # 4
    print(s.maxActiveSectionsAfterTrade("1000100")) # 7
    print(s.maxActiveSectionsAfterTrade("01010")) # 4