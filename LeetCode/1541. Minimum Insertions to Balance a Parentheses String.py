"""
1541. Minimum Insertions to Balance a Parentheses String
Medium
Topics
premium lock icon
Companies
Hint
Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.

 

Example 1:

Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.
Example 2:

Input: s = "())"
Output: 0
Explanation: The string is already balanced.
Example 3:

Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
 

Constraints:

1 <= s.length <= 105
s consists of '(' and ')' only.
"""

class Solution:
    def minInsertions(self, s: str) -> int:
        balance = 0  # Number of unmatched '('
        insertions = 0  # Number of insertions needed

        i = 0
        while i < len(s):
            if s[i] == '(':
                balance += 1
            else:  # s[i] == ')'
                if balance > 0:
                    balance -= 1
                else:
                    insertions += 1  # Need to insert a '(' before this ')'
                
                # Check for the next character to see if we have a pair of ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1  # Skip the next ')' since it's part of the pair
                else:
                    insertions += 1  # Need to insert an additional ')' to make it a pair

            i += 1

        # If there are unmatched '(', we need to add '))' for each unmatched '('
        insertions += balance * 2

        return insertions

if __name__ == "__main__":
    s = Solution()
    print(s.minInsertions("(()))"))  # Output: 1
    print(s.minInsertions("())"))    # Output: 0
    print(s.minInsertions("))())("))  # Output: 3