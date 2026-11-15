"""
2089. Find Target Indices After Sorting Array
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.
Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i], target <= 100
"""

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if n==target:
                res.append(i)
        return res
    
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        return [i for i, x in enumerate(nums) if x == target]

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        lenn = len(nums)
        l, r = 0, lenn - 1
        ans = []
        ans_set = set()
        if nums[l] == nums[r] and nums[l] == target:
            return list(range(0, lenn))
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                ans_set.add(mid)
                if mid + 1 < lenn and nums[mid + 1] == target:
                    ans_set.add(mid + 1)
                if mid + 2 < lenn and nums[mid + 2] == target:
                    ans_set.add(mid + 2)
                if mid - 1 > 0 and nums[mid - 1] == target:
                    ans_set.add(mid - 1)
                r = mid - 1
        ans = sorted(list(ans_set))
        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,5,2,3]
    target = 2
    print(solution.targetIndices(nums, target))  # Output: [1, 2]

    nums = [1,2,5,2,3]
    target = 3
    print(solution.targetIndices(nums, target))  # Output: [3]

    nums = [1,2,5,2,3]
    target = 5
    print(solution.targetIndices(nums, target))  # Output: [4]