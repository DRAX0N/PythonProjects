"""
3727. Maximum Alternating Sum of Squares
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums. You may rearrange the elements in any order.

The alternating score of an array arr is defined as:

score = arr[0]2 - arr[1]2 + arr[2]2 - arr[3]2 + ...
Return an integer denoting the maximum possible alternating score of nums after rearranging its elements.

 

Example 1:

Input: nums = [1,2,3]

Output: 12

Explanation:

A possible rearrangement for nums is [2,1,3], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = 22 - 12 + 32 = 4 - 1 + 9 = 12

Example 2:

Input: nums = [1,-1,2,-2,3,-3]

Output: 16

Explanation:

A possible rearrangement for nums is [-3,-1,-2,1,3,2], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = (-3)2 - (-1)2 + (-2)2 - (1)2 + (3)2 - (2)2 = 9 - 1 + 4 - 1 + 9 - 4 = 16

 

Constraints:

1 <= nums.length <= 105
-4 * 104 <= nums[i] <= 4 * 104
"""
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(x * x for x in nums)
        n = len(nums)
        half = n // 2

        return sum(squares[half:]) - sum(squares[:half])

import numpy as np

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # n = len(nums)
        # nums = sorted(map(abs, nums))
        # return sum(x * x for x in nums[n//2:]) - sum(x * x for x in nums[:n//2])

        sq = np.square(np.array(nums, dtype=np.int64))
        h = len(nums) // 2
        return int(sq.sum() - 2 * np.partition(sq, h)[:h].sum())  # smallest h squares moved to the front, O(n)

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAlternatingSum([1, 2, 3]))  # Output: 12
    print(sol.maxAlternatingSum([1, -1, 2, -2, 3, -3]))  # Output: 16