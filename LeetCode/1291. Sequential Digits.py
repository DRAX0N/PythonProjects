"""
1291. Sequential Digits
Medium
Topics
premium lock icon
Companies
Hint
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
"""
from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for n in range(low, high):
            flag = True
            modulo = n%10 
            temp = n//10
            while temp >= 1:
                if (modulo - 1) == temp%10:
                    modulo = temp%10 
                else:
                    flag = False
                    break
                temp = temp // 10
            if flag == True:
                res.append(n)
        res.sort()
        return  res
    
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        s = "123456789"
        l = str(low)
        h = str(high)

        for length in range(len(l), len(h) + 1):
            for start in range(0, 10 - length):
                num = int(s[start:start + length])
                if low <= num <= high:
                    ans.append(num)

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.sequentialDigits(100, 300)) # [123,234]
    print(s.sequentialDigits(1000, 13000)) # [1234,2345,3456,4567,5678,6789,12345]