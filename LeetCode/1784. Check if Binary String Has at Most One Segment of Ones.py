"""
1784. Check if Binary String Has at Most One Segment of Ones
Easy
Topics
premium lock icon
Companies
Hint
Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

 

Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i]​​​​ is either '0' or '1'.
s[0] is '1'.
"""
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        counter = 0
        for n in range(len(s)):
            if s[n] == "0":
                break
            else:
                counter += 1
        if counter == s.count("1"):
            return True
        else:
            return False
        
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s

if __name__ == "__main__":
    s = "1001"
    print(Solution().checkOnesSegment(s)) # False

    s = "110"
    print(Solution().checkOnesSegment(s)) # True