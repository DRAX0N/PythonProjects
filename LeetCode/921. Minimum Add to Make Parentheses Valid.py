"""
921. Minimum Add to Make Parentheses Valid
Medium
Topics
premium lock icon
Companies
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

 

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
 

Constraints:

1 <= s.length <= 1000
s[i] is either '(' or ')'.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        additions = 0

        for char in s:
            if char == '(':
                balance += 1
            else:  # char == ')'
                if balance > 0:
                    balance -= 1
                else:
                    additions += 1

        return additions + balance

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("())", 1),
        ("(((", 3),
        ("()()", 0),
        (")(", 2),
        ("(()))(", 2)
    ]

    for s, expected in test_cases:
        result = solution.minAddToMakeValid(s)
        assert result == expected, f"Test case failed for input: {s}. Expected: {expected}, Got: {result}"