"""
796. Rotate String
Easy
Topics
premium lock icon
Companies
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if goal == (s[i:]+s[:i]):
                return True
        return False
    
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!= len(goal):
            return False
        
        res=s+s
        if goal in res:
            return True 
        return False
    
if __name__ == "__main__":
    s = "abcde"
    goal = "cdeab"
    print(Solution().rotateString(s, goal))  # True

    s = "abcde"
    goal = "abced"
    print(Solution().rotateString(s, goal))  # False