"""
3753. Total Waviness of Numbers in Range II
Hard
Topics
premium lock icon
Companies
Hint
You are given two integers num1 and num2 representing an inclusive range [num1, num2].

The waviness of a number is defined as the total count of its peaks and valleys:

A digit is a peak if it is strictly greater than both of its immediate neighbors.
A digit is a valley if it is strictly less than both of its immediate neighbors.
The first and last digits of a number cannot be peaks or valleys.
Any number with fewer than 3 digits has a waviness of 0.
Return the total sum of waviness for all numbers in the range [num1, num2].
 

Example 1:

Input: num1 = 120, num2 = 130

Output: 3

Explanation:

In the range [120, 130]:

120: middle digit 2 is a peak, waviness = 1.
121: middle digit 2 is a peak, waviness = 1.
130: middle digit 3 is a peak, waviness = 1.
All other numbers in the range have a waviness of 0.
Thus, total waviness is 1 + 1 + 1 = 3.

Example 2:

Input: num1 = 198, num2 = 202

Output: 3

Explanation:

In the range [198, 202]:

198: middle digit 9 is a peak, waviness = 1.
201: middle digit 0 is a valley, waviness = 1.
202: middle digit 0 is a valley, waviness = 1.
All other numbers in the range have a waviness of 0.
Thus, total waviness is 1 + 1 + 1 = 3.

Example 3:

Input: num1 = 4848, num2 = 4848

Output: 2

Explanation:

Number 4848: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.

 

Constraints:

1 <= num1 <= num2 <= 1015​​​​​​​

"""
#Use digit dynamic programming

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0

        if num2 <= 100:
            return 0
        
        for n in range(num1, num2+1):
            temp = [int(ch) for ch in str(n)]

            for i in range(1,len(temp)-1):
                if temp[i] > temp[i-1] and temp[i] > temp[i+1]:
                    count += 1
                elif temp[i] < temp[i-1] and temp[i] < temp[i+1]:
                    count += 1
                else:
                    continue

        return count
    
from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n: int) -> int:
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dp(pos: int, tight: bool, started: bool, prev2: int, prev1: int):
                # zwraca parę:
                # (ile liczb da się zbudować od tego stanu,
                #  jaka jest łączna waviness tych liczb)
                if pos == m:
                    return (1, 0) if started else (0, 0)

                limit = digits[pos] if tight else 9
                total_count = 0
                total_wavy = 0

                for d in range(limit + 1):
                    new_tight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(pos + 1, new_tight, False, -1, -1)
                        total_count += cnt
                        total_wavy += wav
                    elif not started:
                        cnt, wav = dp(pos + 1, new_tight, True, -1, d)
                        total_count += cnt
                        total_wavy += wav
                    elif prev2 == -1:
                        cnt, wav = dp(pos + 1, new_tight, True, prev1, d)
                        total_count += cnt
                        total_wavy += wav
                    else:
                        add = 1 if ((prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d)) else 0
                        cnt, wav = dp(pos + 1, new_tight, True, prev1, d)
                        total_count += cnt
                        total_wavy += wav + add * cnt

                return total_count, total_wavy

            return dp(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)
    

if __name__ == "__main__":
    s = Solution()
    print(s.totalWaviness(120, 130))  # Output: 3
    print(s.totalWaviness(198, 202))  # Output: 3
    print(s.totalWaviness(4848, 4848))  # Output: 2
    print(s.totalWaviness(2816065, 6679088))  # Output: 11274294