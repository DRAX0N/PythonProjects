"""
Valid Parentheses
Easy
Topics
Company Tags
Hints
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000
"""
class Solution:
    def isValid(self, s: str) -> bool:
        open_para = ["(","[","{"]
        close_para = [")","]","}"]
        bracket_to_close = []
        if_para = False
        for ch in s:
            if ch in open_para:
                bracket_to_close.append(open_para.index(ch))
                if_para = True
            elif ch in close_para:
                if bracket_to_close != [] and close_para.index(ch) == bracket_to_close[-1]:
                    bracket_to_close.pop()
                else:
                    return False

        if bracket_to_close == [] and if_para:
            return True
        else:
            return False
            



if __name__ == "__main__":
    nums="])"
    new = Solution()
    print(new.isValid(nums))