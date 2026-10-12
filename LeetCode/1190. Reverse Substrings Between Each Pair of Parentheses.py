"""
1190. Reverse Substrings Between Each Pair of Parentheses
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
 

Constraints:

1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.
"""
from typing import List
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()  # Remove the '(' from the stack
                stack.extend(temp)  # Add the reversed substring back to the stack
            else:
                stack.append(char)
        return ''.join(stack)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]

        for ch in s:
            if ch == '(':
                stack.append("")
            elif ch == ')':
                temp = stack.pop()
                stack[-1] += temp[::-1]
            else:
                stack[-1] += ch

        return stack[0]
    
if __name__ == "__main__":
    s = Solution()
    print(s.reverseParentheses("(abcd)"))  # Output: "dcba"
    print(s.reverseParentheses("(u(love)i)"))  # Output: "iloveu"
    print(s.reverseParentheses("(ed(et(oc))el)"))  # Output: "leetcode"
