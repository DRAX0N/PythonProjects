"""
1081. Smallest Subsequence of Distinct Characters
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
 
"""

#class Solution:
#    def smallestSubsequence(self, s: str) -> str:
#        temp = set(s)
#        len_temp = len(temp)
#        curr = "zzzzzzzzzzzzzzzzzzz"
#        for i in range(len(s) - len_temp+1):
#            if len(set(s[i:len_temp+i])) == len_temp:
#                for j in range(len_temp):
#                    if curr[j]<s[i:len_temp+i][j]:
#                        break
#                    elif s[i:len_temp+i][j]<curr[j]:
#                        curr = s[i:len_temp+i]
#                        break
#                    else:
#                        continue
#        return curr
    
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stack = []
        used = set()

        for i, c in enumerate(s):
            if c in used:
                continue
            while stack and stack[-1] > c and last[stack[-1]] > i:
                used.remove(stack.pop())
            stack.append(c)
            used.add(c)

        return ''.join(stack)
    
if __name__ == "__main__":
    s = Solution()
    print(s.smallestSubsequence("bcabc")) #"abc"
    print(s.smallestSubsequence("cbacdcbc")) #"acdb"