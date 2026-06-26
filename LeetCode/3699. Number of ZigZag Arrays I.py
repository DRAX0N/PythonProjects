"""
3699. Number of ZigZag Arrays I
Hard
Topics
premium lock icon
Companies
Hint
You are given three integers n, l, and r.

A ZigZag array of length n is defined as follows:

Each element lies in the range [l, r].
No two adjacent elements are equal.
No three consecutive elements form a strictly increasing or strictly decreasing sequence.
Return the total number of valid ZigZag arrays.

Since the answer may be large, return it modulo 109 + 7.

A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).

 

Example 1:

Input: n = 3, l = 4, r = 5

Output: 2

Explanation:

There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:

[4, 5, 4]
[5, 4, 5]​​​​​​​
Example 2:

Input: n = 3, l = 1, r = 3

Output: 10

Explanation:

There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:

[1, 2, 1], [1, 3, 1], [1, 3, 2]
[2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
[3, 1, 2], [3, 1, 3], [3, 2, 3]
All arrays meet the ZigZag conditions.

 

Constraints:

3 <= n <= 2000
1 <= l < r <= 2000
"""

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m % MOD

        up = [0] * m
        down = [0] * m

        for i in range(m):
            up[i] = i
            down[i] = m - 1 - i

        for _ in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m

            pref_down = [0] * m
            pref_down[0] = down[0]
            for i in range(1, m):
                pref_down[i] = (pref_down[i - 1] + down[i]) % MOD

            suf_up = [0] * m
            suf_up[-1] = up[-1]
            for i in range(m - 2, -1, -1):
                suf_up[i] = (suf_up[i + 1] + up[i]) % MOD

            for y in range(m):
                new_up[y] = pref_down[y - 1] if y > 0 else 0
                new_down[y] = suf_up[y + 1] if y + 1 < m else 0

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD

if __name__ == "__main__":
    print(Solution().zigZagArrays(3,4,5)) #2
    print(Solution().zigZagArrays(3,1,3)) #10