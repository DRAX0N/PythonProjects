"""
3488. Closest Equal Element Queries
Medium
Topics
premium lock icon
Companies
Hint
You are given a circular array nums and an array queries.

For each query i, you have to find the following:

The minimum distance between the element at index queries[i] and any other index j in the circular array, where nums[j] == nums[queries[i]]. If no such index exists, the answer for that query should be -1.
Return an array answer of the same size as queries, where answer[i] represents the result for query i.

 

Example 1:

Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]

Output: [2,-1,3]

Explanation:

Query 0: The element at queries[0] = 0 is nums[0] = 1. The nearest index with the same value is 2, and the distance between them is 2.
Query 1: The element at queries[1] = 3 is nums[3] = 4. No other index contains 4, so the result is -1.
Query 2: The element at queries[2] = 5 is nums[5] = 3. The nearest index with the same value is 1, and the distance between them is 3 (following the circular path: 5 -> 6 -> 0 -> 1).
Example 2:

Input: nums = [1,2,3,4], queries = [0,1,2,3]

Output: [-1,-1,-1,-1]

Explanation:

Each value in nums is unique, so no index shares the same value as the queried element. This results in -1 for all queries.

 

Constraints:

1 <= queries.length <= nums.length <= 105
1 <= nums[i] <= 106
0 <= queries[i] < nums.length
"""
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        res = []
        #expected output code below should achieve is in comment where function is called
        for query in queries:
            target = nums[query]
            min_dist = float("inf")
            for index in range(n):
                if index != query and nums[index] == target:
                    dist = min(abs(index-query), n-abs(index-query))
                    min_dist = min(min_dist, dist)
            res.append(min_dist if min_dist != float("inf") else -1)
        return res
    
from typing import List
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = 2 * n
        d = [m] * m

        left = {}
        for i in range(m):
            x = nums[i % n]
            if x in left:
                d[i] = min(d[i], i - left[x])
            left[x] = i

        right = {}
        for i in range(m - 1, -1, -1):
            x = nums[i % n]
            if x in right:
                d[i] = min(d[i], right[x] - i)
            right[x] = i

        for i in range(n):
            d[i] = min(d[i], d[i + n])

        return [-1 if d[q] >= n else d[q] for q in queries]
    
if __name__ == "__main__":
    nums = [1,3,1,4,1,3,2]
    queries = [0,3,5]
    print(Solution().solveQueries(nums, queries)) # [2,-1,3]
    nums = [1,2,3,4]
    queries = [0,1,2,3]
    print(Solution().solveQueries(nums, queries)) # [-1,-1,-1,-1]
    