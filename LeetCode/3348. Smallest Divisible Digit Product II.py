"""
3348. Smallest Divisible Digit Product II
Hard
Topics
premium lock icon
Companies
Hint
You are given a string num which represents a positive integer, and an integer t.

A number is called zero-free if none of its digits are 0.

Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return "-1".

 

Example 1:

Input: num = "1234", t = 256

Output: "1488"

Explanation:

The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

Example 2:

Input: num = "12355", t = 50

Output: "12355"

Explanation:

12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

Example 3:

Input: num = "11111", t = 26

Output: "-1"

Explanation:

No number greater than 11111 has the product of its digits divisible by 26.

 

Constraints:

2 <= num.length <= 2 * 105
num consists only of digits in the range ['0', '9'].
num does not contain leading zeros.
1 <= t <= 1014
"""

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def check_div(str_n):
            number = int(str_n[0])
            for i in str_n[1:]:
                number*=int(i)
            if number%t == 0:
                return True
            else:
                return False
            
        def search_smallest_div(n, t):
            for j in range(1,t):
                if check_div(str(int(n)+j)):
                    if "0" in str(int(n)+j):
                        continue
                    else:
                        return str(int(n)+j)
                else: 
                    continue
            return "-1" 

        if check_div(num):
            if "0" in num:
                return search_smallest_div(num,t)
            else:
                return num
        else:
            return search_smallest_div(num,t)

import math

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        for i in range(2, 10):
            while temp % i == 0:
                temp //= i

        if temp > 1:
            return "-1"

        n = len(num)
        rem = [0] * (n + 1)
        rem[0] = t
        pos = n - 1

        num_list = list(num)
        for i in range(n):
            if num_list[i] == "0":
                pos = i
                break
            rem[i + 1] = rem[i] // math.gcd(rem[i], int(num_list[i]))

        if rem[n] == 1:
            return num

        for i in range(pos, -1, -1):
            while True:
                num_list[i] = chr(ord(num_list[i]) + 1)
                if num_list[i] > "9":
                    break

                t_now = rem[i] // math.gcd(rem[i], int(num_list[i]))
                k = 9

                for j in range(n - 1, i, -1):
                    while t_now % k != 0:
                        k -= 1
                    t_now //= k
                    num_list[j] = str(k)

                if t_now == 1:
                    return "".join(num_list)

        ans = []
        original_t = t
        for i in range(9, 1, -1):
            while original_t % i == 0:
                ans.append(str(i))
                original_t //= i

        ans_str = "".join(ans)
        padding = max(n + 1 - len(ans_str), 0)
        ans_str += "1" * padding

        return ans_str[::-1]

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def build_end(req, size):
            res = []
            for f in range(9, 1, -1):
                while req % f == 0:
                    req //= f
                    res.append(str(f))
            if len(res) < size: res += ['1'] * (size - len(res))
            return "".join(res[::-1])        
        
        n = len(num)

        curr = t
        for f in [2, 3, 5, 7]:
            while curr % f == 0:
                curr //= f
        if curr != 1: return '-1'

        rem = [0] * (n + 1)
        rem[0] = t
        for i in range(n):
            if num[i] == '0': break
            rem[i + 1] = rem[i] // gcd(rem[i], int(num[i]))
        if rem[-1] == 1: return num

        z = num.find('0')
        start = z if z != -1 else n - 1

        for i in range(start, -1, -1):
            end_size = n - i - 1
            for d in range(int(num[i]) + 1, 10):
                last = build_end(rem[i] // gcd(rem[i], d), end_size)
                if len(last) == end_size: return num[:i] + str(d) + last
        
        return build_end(t, n + 1)

if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestNumber("1234", 256))  # Output: "1488"
    print(solution.smallestNumber("12355", 50))  # Output: "12355"
    print(solution.smallestNumber("11111", 26))  # Output: "-1"