"""
2948. Make Lexicographically Smallest Array by Swapping Elements
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed array of positive integers nums and a positive integer limit.

In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.

 

Example 1:

Input: nums = [1,5,3,9,8], limit = 2
Output: [1,3,5,8,9]
Explanation: Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.
Example 2:

Input: nums = [1,7,6,18,2,1], limit = 3
Output: [1,6,7,18,1,2]
Explanation: Apply the operation 3 times:
- Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
- Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
- Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
We cannot obtain a lexicographically smaller array by applying any more operations.
Example 3:

Input: nums = [1,7,28,19,10], limit = 3
Output: [1,7,28,19,10]
Explanation: [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= limit <= 109
"""
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        # Pair each number with its original index and sort by value
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))

        # Group indices by connected components in value-sorted order
        groups = []
        current_group_vals = []
        current_group_idxs = []

        prev_val, prev_idx = sorted_nums[0]
        current_group_vals.append(prev_val)
        current_group_idxs.append(prev_idx)

        for val, idx in sorted_nums[1:]:
            if val - prev_val <= limit:
                # Same component
                current_group_vals.append(val)
                current_group_idxs.append(idx)
            else:
                # Finish current group and start a new one
                groups.append((current_group_vals, current_group_idxs))
                current_group_vals = [val]
                current_group_idxs = [idx]
            prev_val = val

        # Append the last group
        groups.append((current_group_vals, current_group_idxs))

        # Build the result array
        result = [0] * n
        for vals, idxs in groups:
            # Sort indices to place smallest values in the earliest positions
            sorted_idxs = sorted(idxs)
            sorted_vals = sorted(vals)  # vals are already sorted by construction, but explicit for clarity
            for i, v in zip(sorted_idxs, sorted_vals):
                result[i] = v

        return result

if __name__ == "__main__":
    solution = Solution()
    nums = [1,5,3,9,8]
    limit = 2
    result = solution.lexicographicallySmallestArray(nums, limit)
    print(result)  # Output: [1,3,5,8,9]

    nums = [1,7,6,18,2,1]
    limit = 3
    result = solution.lexicographicallySmallestArray(nums, limit)
    print(result)  # Output: [1,6,7,18,1,2]

    nums = [1,7,28,19,10]
    limit = 3
    result = solution.lexicographicallySmallestArray(nums, limit)
    print(result)  # Output: [1,7,28,19,10]