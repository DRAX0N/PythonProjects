"""
3700. Number of ZigZag Arrays II
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
[5, 4, 5]
Example 2:

Input: n = 3, l = 1, r = 3

Output: 10

Explanation:

​​​​​​​There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:

[1, 2, 1], [1, 3, 1], [1, 3, 2]
[2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
[3, 1, 2], [3, 1, 3], [3, 2, 3]
All arrays meet the ZigZag conditions.

 

Constraints:

3 <= n <= 109
1 <= l < r <= 75​​​​​​​
"""

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m % MOD

        def step(up, down):
            new_down = [0] * m
            new_up = [0] * m

            pref = 0
            for y in range(m):
                new_down[y] = pref
                pref = (pref + up[y]) % MOD

            suf = 0
            for y in range(m - 1, -1, -1):
                new_up[y] = suf
                suf = (suf + down[y]) % MOD

            return new_up, new_down

        up = [1] * m
        down = [1] * m

        k = n - 1
        while k:
            up, down = step(up, down)
            k -= 1
            if k == 0:
                break

        return (sum(up) + sum(down)) % MOD
    
    
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m % MOD

        size = 2 * m

        def idx(kind, x):
            return kind * m + x

        T = [[0] * size for _ in range(size)]

        for x in range(m):
            for y in range(x + 1, m):
                T[idx(1, y)][idx(0, x)] = 1
            for y in range(0, x):
                T[idx(0, y)][idx(1, x)] = 1

        def mat_mul(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                Ai = A[i]
                Ci = C[i]
                for k in range(size):
                    if Ai[k]:
                        v = Ai[k]
                        Bk = B[k]
                        for j in range(size):
                            if Bk[j]:
                                Ci[j] = (Ci[j] + v * Bk[j]) % MOD
            return C

        def mat_vec_mul(A, v):
            res = [0] * size
            for i in range(size):
                s = 0
                Ai = A[i]
                for j in range(size):
                    if Ai[j]:
                        s = (s + Ai[j] * v[j]) % MOD
                res[i] = s
            return res

        def mat_pow(A, e):
            R = [[0] * size for _ in range(size)]
            for i in range(size):
                R[i][i] = 1
            while e:
                if e & 1:
                    R = mat_mul(R, A)
                A = mat_mul(A, A)
                e >>= 1
            return R

        start = [1] * size
        P = mat_pow(T, n - 1)
        final = mat_vec_mul(P, start)
        return sum(final) % MOD
    
if __name__ == "__main__":
    print(Solution().zigZagArrays(3,4,5)) #2
    print(Solution().zigZagArrays(3,1,3)) #10