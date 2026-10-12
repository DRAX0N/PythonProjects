"""
301. Remove Invalid Parentheses
Hard
Topics
premium lock icon
Companies
Hint
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]
 

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string):
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        level = {s}
        while True:
            valid_strings = list(filter(is_valid, level))
            if valid_strings:
                return valid_strings
            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in '()':
                        next_level.add(string[:i] + string[i + 1:])
            level = next_level

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("()())()", ["(())()", "()()()"]),
        ("(a)())()", ["(a())()", "(a)()()"]),
        (")(", [""]),
        ("(((", [""]),
        ("", [""])
    ]
    for i, (input_str, expected) in enumerate(test_cases):
        result = solution.removeInvalidParentheses(input_str)
        print(f"Test case {i + 1}:")
        print(f"Input: {input_str}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Passed: {sorted(result) == sorted(expected)}")
        print()