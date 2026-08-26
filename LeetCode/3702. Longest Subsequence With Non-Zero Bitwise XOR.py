"""
3702. Longest Subsequence With Non-Zero Bitwise XOR
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.

 

Example 1:

Input: nums = [1,2,3]

Output: 2

Explanation:

One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.

Example 2:

Input: nums = [2,3,4]

Output: 3

Explanation:

The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.

 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
"""

from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        tot = nz = 0

        for n in nums:
            nz |= n > 0
            tot ^= n

        return nz * (len(nums) - (not tot))
        

if __name__ == "__main__":
    s = Solution()
    print(s.longestSubsequence([1, 2, 3]))  # Output: 2
    print(s.longestSubsequence([2, 3, 4]))  # Output: 3
    print(s.longestSubsequence([0, 0, 0]))  # Output: 0