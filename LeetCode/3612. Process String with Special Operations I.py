"""
3612. Process String with Special Operations I
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s consisting of lowercase English letters and the special characters: *, #, and %.

Build a new string result by processing s according to the following rules from left to right:

If the letter is a lowercase English letter append it to result.
A '*' removes the last character from result, if it exists.
A '#' duplicates the current result and appends it to itself.
A '%' reverses the current result.
Return the final string result after processing all characters in s.

 

Example 1:

Input: s = "a#b%*"

Output: "ba"

Explanation:

i	s[i]	Operation	Current result
0	'a'	Append 'a'	"a"
1	'#'	Duplicate result	"aa"
2	'b'	Append 'b'	"aab"
3	'%'	Reverse result	"baa"
4	'*'	Remove the last character	"ba"
Thus, the final result is "ba".

Example 2:

Input: s = "z*#"

Output: ""

Explanation:

i	s[i]	Operation	Current result
0	'z'	Append 'z'	"z"
1	'*'	Remove the last character	""
2	'#'	Duplicate the string	""
Thus, the final result is "".

 

Constraints:

1 <= s.length <= 20
s consists of only lowercase English letters and special characters *, #, and %.
"""

class Solution:
    def processStr(self, s: str) -> str:
        temp = [ch for ch in s]
        #print(temp[-1::-1])
        result = ""
        for ch in temp:
            if ord("a")<=ord(ch)<=ord("z"):
                result += ch
            elif ch == '*' and result != "":
                result = result[:-1]
            elif ch == '#':
                result += result
            elif ch == '%':
                result = result[::-1]
        return result

if __name__ == "__main__":
    print(Solution().processStr("a#b%*")) #"ba"
    print(Solution().processStr("z*#")) #""