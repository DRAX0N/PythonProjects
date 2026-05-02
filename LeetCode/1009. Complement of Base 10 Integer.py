"""
1009. Complement of Base 10 Integer
Easy
Topics
premium lock icon
Companies
Hint
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.

 

Example 1:

Input: n = 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:

Input: n = 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:

Input: n = 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 

Constraints:

0 <= n < 109
 

Note: This question is the same as 476: https://leetcode.com/problems/number-complement/

"""

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_n = bin(n)[2:]
        com_bin_n = "".join(["0" if ch == "1" else "1" for ch in bin_n])
        return int(com_bin_n,2)
    
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        mask = 0
        x = n
        while x:
            mask = (mask << 1) | 1
            x >>= 1
        
        return mask ^ n
    
if __name__ == "__main__":
    n = 5
    print(Solution().bitwiseComplement(n)) # 2
    n = 7
    print(Solution().bitwiseComplement(n)) # 0
    n = 10
    print(Solution().bitwiseComplement(n)) # 5