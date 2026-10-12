"""
3525. Find X Value of Array II
Hard
Topics
premium lock icon
Companies
Hint
You are given an array of positive integers nums and a positive integer k. You are also given a 2D array queries, where queries[i] = [indexi, valuei, starti, xi].

You are allowed to perform an operation once on nums, where you can remove any suffix from nums such that nums remains non-empty.

The x-value of nums for a given x is defined as the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x modulo k.

For each query in queries you need to determine the x-value of nums for xi after performing the following actions:

Update nums[indexi] to valuei. Only this step persists for the rest of the queries.
Remove the prefix nums[0..(starti - 1)] (where nums[0..(-1)] will be used to represent the empty prefix).
Return an array result of size queries.length where result[i] is the answer for the ith query.

A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.

A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.

Note that the prefix and suffix to be chosen for the operation can be empty.

Note that x-value has a different definition in this version.

 

Example 1:

Input: nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]

Output: [2,2,2]

Explanation:

For query 0, nums becomes [1, 2, 2, 4, 5], and the empty prefix must be removed. The possible operations are:
Remove the suffix [2, 4, 5]. nums becomes [1, 2].
Remove the empty suffix. nums becomes [1, 2, 2, 4, 5] with a product 80, which gives remainder 2 when divided by 3.
For query 1, nums becomes [1, 2, 2, 3, 5], and the prefix [1, 2, 2] must be removed. The possible operations are:
Remove the empty suffix. nums becomes [3, 5].
Remove the suffix [5]. nums becomes [3].
For query 2, nums becomes [1, 2, 2, 3, 5], and the empty prefix must be removed. The possible operations are:
Remove the suffix [2, 2, 3, 5]. nums becomes [1].
Remove the suffix [3, 5]. nums becomes [1, 2, 2].
Example 2:

Input: nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]]

Output: [1,0]

Explanation:

For query 0, nums becomes [2, 2, 4, 8, 16, 32]. The only possible operation is:
Remove the suffix [2, 4, 8, 16, 32].
For query 1, nums becomes [2, 2, 4, 8, 16, 32]. There is no possible way to perform the operation.
Example 3:

Input: nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]]

Output: [5]

 

Constraints:

1 <= nums[i] <= 109
1 <= nums.length <= 105
1 <= k <= 5
1 <= queries.length <= 2 * 104
queries[i] == [indexi, valuei, starti, xi]
0 <= indexi <= nums.length - 1
1 <= valuei <= 109
0 <= starti <= nums.length - 1
0 <= xi <= k - 1
"""

from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        
        # Each node: (prod, cnt) where cnt is list of length k
        # Tree size: 4*n
        tree_prod = [1] * (4 * n)
        tree_cnt = [[0] * k for _ in range(4 * n)]
        
        def build(node: int, l: int, r: int) -> None:
            if l == r:
                val = nums[l] % k
                tree_prod[node] = val
                tree_cnt[node] = [0] * k
                tree_cnt[node][val] = 1
                return
            
            mid = (l + r) // 2
            left_node = 2 * node
            right_node = 2 * node + 1
            
            build(left_node, l, mid)
            build(right_node, mid + 1, r)
            
            # Merge
            lp, rp = tree_prod[left_node], tree_prod[right_node]
            tree_prod[node] = (lp * rp) % k
            
            cnt = [0] * k
            # Left prefixes
            for i in range(k):
                cnt[i] += tree_cnt[left_node][i]
            # Right prefixes shifted by left product
            for i in range(k):
                cnt[(lp * i) % k] += tree_cnt[right_node][i]
            
            tree_cnt[node] = cnt
        
        def update(node: int, l: int, r: int, idx: int, val: int) -> None:
            if l == r:
                v = val % k
                tree_prod[node] = v
                tree_cnt[node] = [0] * k
                tree_cnt[node][v] = 1
                return
            
            mid = (l + r) // 2
            left_node = 2 * node
            right_node = 2 * node + 1
            
            if idx <= mid:
                update(left_node, l, mid, idx, val)
            else:
                update(right_node, mid + 1, r, idx, val)
            
            # Merge
            lp, rp = tree_prod[left_node], tree_prod[right_node]
            tree_prod[node] = (lp * rp) % k
            
            cnt = [0] * k
            for i in range(k):
                cnt[i] += tree_cnt[left_node][i]
            for i in range(k):
                cnt[(lp * i) % k] += tree_cnt[right_node][i]
            
            tree_cnt[node] = cnt
        
        def query(node: int, l: int, r: int, ql: int, qr: int) -> tuple:
            """Return (prod, cnt) for range [ql, qr]"""
            if ql <= l and r <= qr:
                return tree_prod[node], tree_cnt[node]
            
            mid = (l + r) // 2
            left_node = 2 * node
            right_node = 2 * node + 1
            
            if qr <= mid:
                return query(left_node, l, mid, ql, qr)
            if ql > mid:
                return query(right_node, mid + 1, r, ql, qr)
            
            # Merge results from both children
            lp, lcnt = query(left_node, l, mid, ql, qr)
            rp, rcnt = query(right_node, mid + 1, r, ql, qr)
            
            prod = (lp * rp) % k
            cnt = [0] * k
            for i in range(k):
                cnt[i] += lcnt[i]
            for i in range(k):
                cnt[(lp * i) % k] += rcnt[i]
            
            return prod, cnt
        
        # Build tree
        build(1, 0, n - 1)
        
        result = []
        for idx, val, start, x in queries:
            # Update
            update(1, 0, n - 1, idx, val)
            # Query range [start, n-1]
            _, cnt = query(1, 0, n - 1, start, n - 1)
            result.append(cnt[x])
        
        return result

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5]
    k = 3
    queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]
    print(sol.resultArray(nums, k, queries))  # Output: [2,2,2]

    nums2 = [1,2,4,8,16,32]
    k2 = 4
    queries2 = [[0,2,0,2],[0,2,0,1]]
    print(sol.resultArray(nums2, k2, queries2))  # Output: [1,0]