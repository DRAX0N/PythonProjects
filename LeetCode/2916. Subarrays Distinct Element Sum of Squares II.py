"""
2916. Subarrays Distinct Element Sum of Squares II
Hard
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.
Example 2:

Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
"""
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        s = [0] * (4 * n)    # suma d[l]
        s2 = [0] * (4 * n)   # suma d[l]^2
        lazy = [0] * (4 * n)

        def apply(node: int, length: int, v: int) -> None:
            s2[node] = (s2[node] + 2 * v * s[node] + v * v * length) % MOD
            s[node] = (s[node] + v * length) % MOD
            lazy[node] = (lazy[node] + v) % MOD

        def push(node: int, nl: int, nr: int) -> None:
            if lazy[node]:
                mid = (nl + nr) // 2
                apply(2 * node, mid - nl + 1, lazy[node])
                apply(2 * node + 1, nr - mid, lazy[node])
                lazy[node] = 0

        def update(node: int, nl: int, nr: int, l: int, r: int, v: int) -> None:
            if r < nl or nr < l:
                return
            if l <= nl and nr <= r:
                apply(node, nr - nl + 1, v)
                return

            push(node, nl, nr)
            mid = (nl + nr) // 2
            update(2 * node, nl, mid, l, r, v)
            update(2 * node + 1, mid + 1, nr, l, r, v)

            s[node] = (s[2 * node] + s[2 * node + 1]) % MOD
            s2[node] = (s2[2 * node] + s2[2 * node + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            l = last.get(x, -1) + 1
            update(1, 0, n - 1, l, i, 1)
            ans = (ans + s2[1]) % MOD
            last[x] = i

        return ans

    
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        SHIFT = 40
        MASK = (1 << SHIFT) - 1
        bit = [0] * (n + 1)
        last = {}
        totC = 0
        totS = 0
        g = 0
        ans = 0
        for j in range(n):
            v = nums[j]
            p = last.get(v, -1)
            if p < 0:
                R = totS + totC
            else:
                i = p + 1
                q = 0
                while i > 0:
                    q += bit[i]
                    i -= i & (-i)
                cSuf = totC - (q >> SHIFT)
                sSuf = totS - (q & MASK)
                R = sSuf - p * cSuf
                d = -((1 << SHIFT) + p)
                i = p + 1
                while i <= n:
                    bit[i] += d
                    i += i & (-i)
                totC -= 1
                totS -= p
            d = (1 << SHIFT) + j
            i = j + 1
            while i <= n:
                bit[i] += d
                i += i & (-i)
            totC += 1
            totS += j
            g += 2 * R + (j - p)
            ans += g
            last[v] = j
        return ans % MOD
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 1]
    print(solution.sumCounts(nums1))  # Output: 15

    nums2 = [2, 2]
    print(solution.sumCounts(nums2))  # Output: 3