"""
3629. Minimum Jumps to Reach End via Prime Teleportation
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of length n.

You start at index 0, and your goal is to reach index n - 1.

From any index i, you may perform one of the following operations:

Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.
Return the minimum number of jumps required to reach index n - 1.

 

Example 1:

Input: nums = [1,2,4,6]

Output: 2

Explanation:

One optimal sequence of jumps is:

Start at index i = 0. Take an adjacent step to index 1.
At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.
Thus, the answer is 2.

Example 2:

Input: nums = [2,3,4,7,9]

Output: 2

Explanation:

One optimal sequence of jumps is:

Start at index i = 0. Take an adjacent step to index i = 1.
At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.
Thus, the answer is 2.

Example 3:

Input: nums = [4,6,5,8]

Output: 3

Explanation:

Since no teleportation is possible, we move through 0 → 1 → 2 → 3. Thus, the answer is 3.
 

Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= 106
"""

from collections import deque, defaultdict
from math import isqrt
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        max_val = max(nums)

        is_prime = [True] * (max_val + 1)
        if max_val >= 0:
            is_prime[0] = False
        if max_val >= 1:
            is_prime[1] = False

        for p in range(2, isqrt(max_val) + 1):
            if is_prime[p]:
                for x in range(p * p, max_val + 1, p):
                    is_prime[x] = False

        prime_to_indices = defaultdict(list)
        for idx, val in enumerate(nums):
            if val > 1:
                x = val
                seen = set()
                d = 2
                while d * d <= x:
                    if x % d == 0:
                        if is_prime[d] and d not in seen:
                            prime_to_indices[d].append(idx)
                            seen.add(d)
                        while x % d == 0:
                            x //= d
                    d += 1
                if x > 1 and is_prime[x] and x not in seen:
                    prime_to_indices[x].append(idx)

        q = deque([0])
        dist = [-1] * n
        dist[0] = 0
        used_prime = set()

        while q:
            i = q.popleft()
            d = dist[i]

            if i == n - 1:
                return d

            for ni in (i - 1, i + 1):
                if 0 <= ni < n and dist[ni] == -1:
                    dist[ni] = d + 1
                    q.append(ni)

            p = nums[i]
            if p > 1 and is_prime[p] and p not in used_prime:
                used_prime.add(p)
                for ni in prime_to_indices.get(p, []):
                    if dist[ni] == -1:
                        dist[ni] = d + 1
                        q.append(ni)
                prime_to_indices[p].clear()

        return -1

MX = 1_000_001
factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not factors[i]:
        for j in range(i, MX, i):
            factors[j].append(i)


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        edges = defaultdict(list)
        for i, a in enumerate(nums):
            if len(factors[a]) == 1:
                edges[a].append(i)
        res = 0
        seen = [False] * n
        seen[-1] = True
        q = [n - 1]
        while True:
            q2 = []
            for i in q:
                if i == 0:
                    return res
                if i > 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    q2.append(i - 1)
                if i < n - 1 and not seen[i + 1]:
                    seen[i + 1] = True
                    q2.append(i + 1)
                for p in factors[nums[i]]:
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q2.append(j)
                    edges[p].clear()
            q = q2
            res += 1

            
if __name__ == "__main__":
    s = Solution()
    print(s.minJumps([1,2,4,6]))  # Output: 2
    print(s.minJumps([2,3,4,7,9]))  # Output: 2
    print(s.minJumps([4,6,5,8]))  # Output: 3