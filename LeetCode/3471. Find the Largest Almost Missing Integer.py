"""
3471. Find the Largest Almost Missing Integer
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and an integer k.

An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.

Return the largest almost missing integer from nums. If no such integer exists, return -1.

A subarray is a contiguous sequence of elements within an array.
 

Example 1:

Input: nums = [3,9,2,1,7], k = 3

Output: 7

Explanation:

1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
3 appears in 1 subarray of size 3: [3, 9, 2].
7 appears in 1 subarray of size 3: [2, 1, 7].
9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
We return 7 since it is the largest integer that appears in exactly one subarray of size k.

Example 2:

Input: nums = [3,9,7,2,1,7], k = 4

Output: 3

Explanation:

1 appears in 2 subarrays of size 4: [9, 7, 2, 1], [7, 2, 1, 7].
2 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
3 appears in 1 subarray of size 4: [3, 9, 7, 2].
7 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
9 appears in 2 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1].
We return 3 since it is the largest and only integer that appears in exactly one subarray of size k.

Example 3:

Input: nums = [0,0], k = 1

Output: -1

Explanation:

There is no integer that appears in only one subarray of size 1.

 

Constraints:

1 <= nums.length <= 50
0 <= nums[i] <= 50
1 <= k <= nums.length
"""
from typing import List
from collections import defaultdict
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count_map = defaultdict(int)

        # Count occurrences of each number in all subarrays of size k
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            unique_numbers = set(subarray)
            for num in unique_numbers:
                count_map[num] += 1

        # Find the largest number that appears in exactly one subarray of size k
        largest_almost_missing = -1
        for num, count in count_map.items():
            if count == 1:
                largest_almost_missing = max(largest_almost_missing, num)

        return largest_almost_missing
    
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)

        if k == 1:
            arr = [x for x in nums if nums.count(x) == 1]
        else:
            arr = [x for x in (nums[0], nums[-1]) if nums.count(x) == 1]
        
        return max(arr) if arr else -1
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestInteger([3,9,2,1,7], 3))  # Output: 7
    print(solution.largestInteger([3,9,7,2,1,7], 4))  # Output: 3
    print(solution.largestInteger([0,0], 1))  # Output: -1