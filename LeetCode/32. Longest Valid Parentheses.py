"""
32. Longest Valid Parentheses
Hard
Topics
premium lock icon
Companies
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_length = 0
        last_invalid_index = -1

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if not stack:
                    last_invalid_index = i
                else:
                    stack.pop()
                    if not stack:
                        max_length = max(max_length, i - last_invalid_index)
                    else:
                        max_length = max(max_length, i - stack[-1])

        return max_length    

if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses("(()")) # Expected output: 2
    print(s.longestValidParentheses(")()())")) # Expected output: 4
    print(s.longestValidParentheses("")) # Expected output: 0