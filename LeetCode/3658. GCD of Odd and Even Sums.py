"""
3658. GCD of Odd and Even Sums
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:

sumOdd: the sum of the smallest n positive odd numbers.

sumEven: the sum of the smallest n positive even numbers.

Return the GCD of sumOdd and sumEven.

 

Example 1:

Input: n = 4

Output: 4

Explanation:

Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16
Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20
Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.

Example 2:

Input: n = 5

Output: 5

Explanation:

Sum of the first 5 odd numbers sumOdd = 1 + 3 + 5 + 7 + 9 = 25
Sum of the first 5 even numbers sumEven = 2 + 4 + 6 + 8 + 10 = 30
Hence, GCD(sumOdd, sumEven) = GCD(25, 30) = 5.

 

Constraints:

1 <= n <= 10​​​​​​​00
"""
import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 1
        sumEven = 0
        for i in range(1, n+1):
            sumEven += i*2
            if i < n:
                sumOdd += (i*2)+1
        
        return math.gcd(sumOdd,sumEven)
    
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
    
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = n * n
        sumEven = n * (n + 1)

        res = 0

        bigger = max(sumOdd, sumEven)

        for i in range(1, bigger // 2 + 1):
            if sumOdd % i == 0 and sumEven % i == 0:
                res = i
        
        return res
    
if __name__ == "__main__":
    s = Solution()
    print(s.gcdOfOddEvenSums(4)) #4
    print(s.gcdOfOddEvenSums(5)) #5