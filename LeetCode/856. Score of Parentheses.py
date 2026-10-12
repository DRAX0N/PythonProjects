"""
856. Score of Parentheses
Medium
Topics
premium lock icon
Companies
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
 

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
"""
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0

        for char in s:
            if char == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(2 * score, 1)

        return score

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("()", 1),
        ("(())", 2),
        ("()()", 2)
    ]

    for s, expected in test_cases:
        result = solution.scoreOfParentheses(s)
        assert result == expected, f"Test case failed for input: {s}. Expected: {expected}, Got: {result}"
    print("All test cases passed!")