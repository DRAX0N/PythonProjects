"""
628. Maximum Product of Three Numbers
Easy
Topics
premium lock icon
Companies
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
 

Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
"""
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3]
    print(solution.maximumProduct(nums1))  # Output: 6

    nums2 = [1, 2, 3, 4]
    print(solution.maximumProduct(nums2))  # Output: 24

    nums3 = [-1, -2, -3]
    print(solution.maximumProduct(nums3))  # Output: -6

    nums4 = [-100,-98,-1,2,3,4]
    print(solution.maximumProduct(nums4))  # Output: 39200