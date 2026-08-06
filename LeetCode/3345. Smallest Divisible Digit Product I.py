"""

Code
Testcase
Testcase
Test Result
3345. Smallest Divisible Digit Product I
Easy
Topics
premium lock icon
Companies
Hint
You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.

 

Example 1:

Input: n = 10, t = 2

Output: 10

Explanation:

The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.

Example 2:

Input: n = 15, t = 3

Output: 16

Explanation:

The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.

 

Constraints:

1 <= n <= 100
1 <= t <= 10
"""

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def check_div(n):
            str_n = str(n)
            n_list = [int(number) for number in str_n]
            num = int(str_n[0])
            for i in str_n[1:]:
                num*=int(i)
            if num%t == 0:
                return True
            else:
                return False
        if check_div(n):
            return n
        else:
            for j in range(1,t):
                if check_div(n+j):
                    return n+j
                else: 
                    continue
                
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+1000):
            x=i
            pr=1
            while x>0:
                pr*=x%10
                x//=10
            if pr%t==0:
                return i

if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestNumber(10, 2))  # Output: 10
    print(solution.smallestNumber(15, 3))  # Output: 16