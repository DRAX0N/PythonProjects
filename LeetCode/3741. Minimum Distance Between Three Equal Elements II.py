"""
3741. Minimum Distance Between Three Equal Elements II
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].

The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.

Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

 

Example 1:

Input: nums = [1,2,1,1,3]

Output: 6

Explanation:

The minimum distance is achieved by the good tuple (0, 2, 3).

(0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.

Example 2:

Input: nums = [1,1,2,3,2,1,2]

Output: 8

Explanation:

The minimum distance is achieved by the good tuple (2, 4, 6).

(2, 4, 6) is a good tuple because nums[2] == nums[4] == nums[6] == 2. Its distance is abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8.

Example 3:

Input: nums = [1]

Output: -1

Explanation:

There are no good tuples. Therefore, the answer is -1.

 

Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= n
"""

from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        group = {}
        for i, n in enumerate(nums):
            if n in group.keys():
                group[n].append(i)
            else:
                group[n] = [i]
        res = float("infinity")
        for values in group.values():
            if len(values) == 3:
                res = min(res, (abs(values[0] - values[1]) + abs(values[1] - values[2]) + abs(values[2] - values[0])))
            elif len(values) > 3:
                for n in range(2,len(values)):
                    res = min(res, (abs(values[n-2] - values[n-1]) + abs(values[n-1] - values[n]) + abs(values[n] - values[n-2])))
            else:
                continue
        return -1 if res == float("infinity") else res
    
import math    
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        min_length = len(nums) + 1

        last_indices = [-1] * min_length
        second_to_last_indices = [-1] * min_length

        min_dist = math.inf
        for i, num in enumerate(nums):
            if second_to_last_indices[num] != -1:
                dist = i - second_to_last_indices[num]
                if min_dist > dist:
                    min_dist = dist
            second_to_last_indices[num], last_indices[num] = last_indices[num], i
        if min_dist == math.inf:
            return -1
        return 2 * min_dist

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums = [1,2,1,1,3]
    print(solution.minimumDistance(nums))  # Expected output: 6

    # Test case 2
    nums = [1,1,2,3,2,1,2]
    print(solution.minimumDistance(nums))  # Expected output: 8

    # Test case 3
    nums = [1]
    print(solution.minimumDistance(nums))  # Expected output: -1