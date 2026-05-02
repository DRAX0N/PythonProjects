"""
Valid Palindrome
Easy
Topics
Company Tags
Hints
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""
# first solutyion
#class Solution:
#    def isPalindrome(self, s: str) -> bool:
#        temp = "".join(ch.lower() for ch in s if ch.isalnum())
#        return temp == temp[::-1]

#two pointers    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        numeric_list = [ord(ch.lower()) for ch in s]
        left = 0
        right = len(numeric_list)-1
        isequal = True
        
        while left<=right:
            if ((48 <= numeric_list[left] <= 57) or 97 <= numeric_list[left] <= 122) and ((48 <= numeric_list[right] <= 57) or 97 <= numeric_list[right] <= 122):
                isequal = numeric_list[left]==numeric_list[right]
                left += 1
                right-=1
                if not isequal:
                    return isequal
            elif not (48 <= numeric_list[left] <= 57 or 97 <= numeric_list[left] <= 122):
                left += 1
            else:
                right-=1
                
        return isequal

if __name__ == '__main__':
    s = "Was it a car or a cat I saw?"
    #s="0P"
    s = ".a"

    new = Solution()
    print(new.isPalindrome(s))