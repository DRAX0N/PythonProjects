'''
Given an integer x, return true if x is a palindrome, and false otherwise.
 
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
'''
class Solution:

    #str solution
    #def isPalindrome(self, x: int) -> bool:
    #    s = str(x)
    #    mirror = s[::-1]
    #    if s == mirror:
    #        return True
    #    else:
    #        return False
        
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        work = True
        result = []
        while work:
            reszta = x%10
            x = int(x//10)
            result.append(reszta)
            if x == 0:
                work = False

        if result == result[::-1]:
            return True
        else:
            return False

if __name__ == '__main__':
    new = Solution()
    print(new.isPalindrome(-121))
