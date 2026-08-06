"""
3312. Sorted GCD Pair Queries
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of length n and an integer array queries.

Let gcdPairs denote an array obtained by calculating the GCD of all possible pairs (nums[i], nums[j]), where 0 <= i < j < n, and then sorting these values in ascending order.

For each query queries[i], you need to find the element at index queries[i] in gcdPairs.

Return an integer array answer, where answer[i] is the value at gcdPairs[queries[i]] for each query.

The term gcd(a, b) denotes the greatest common divisor of a and b.

 

Example 1:

Input: nums = [2,3,4], queries = [0,2,2]

Output: [1,2,2]

Explanation:

gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1].

After sorting in ascending order, gcdPairs = [1, 1, 2].

So, the answer is [gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2].

Example 2:

Input: nums = [4,4,2,1], queries = [5,3,1,0]

Output: [4,2,1,1]

Explanation:

gcdPairs sorted in ascending order is [1, 1, 1, 2, 2, 4].

Example 3:

Input: nums = [2,2], queries = [0,0]

Output: [2,2]

Explanation:

gcdPairs = [2].

 

Constraints:

2 <= n == nums.length <= 105
1 <= nums[i] <= 5 * 104
1 <= queries.length <= 105
0 <= queries[i] < n * (n - 1) / 2
"""
from typing import List
from collections import Counter
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        cnt = Counter(nums)

        pairs = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            c = 0
            for x in range(g, mx + 1, g):
                c += cnt[x]

            total = c * (c - 1) // 2

            for m in range(2 * g, mx + 1, g):
                total -= pairs[m]

            pairs[g] = total

        pref = []
        s = 0
        for g in range(1, mx + 1):
            s += pairs[g]
            pref.append(s)

        return [bisect_right(pref, q) + 1 for q in queries]

if __name__ == "__main__":
    s = Solution()
    print(s.gcdValues([2,3,4], [0,2,2])) #[1,2,2]
    print(s.gcdValues([4,4,2,1], [5,3,1,0])) #[4,2,1,1]
    print(s.gcdValues([2,2], [0,0])) #[2,2]