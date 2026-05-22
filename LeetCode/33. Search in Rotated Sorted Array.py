"""
33. Search in Rotated Sorted Array
Solved
Medium
Topics
premium lock icon
Companies
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(nums)
        l, r = 0, len(nums)-1

        while l<=r:
            print("l value = " + str(nums[l]))
            print("r value = " + str(nums[r]))

            mid = (l+r)//2
            print("mid value = " + str(nums[mid]))
            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            
            elif nums[l] <= nums[r]:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[r] > target and nums[mid] > target and nums[r] > nums[mid]:
                    print("1")
                    r = mid - 1
                elif nums[r] > target and nums[mid] > target and nums[r] < nums[mid]:
                    print("2")
                    l = mid + 1
                elif nums[r] > target and nums[mid] < target:
                    print("3")
                    l = mid + 1
                elif nums[r] < target and nums[mid] > target:
                    print("4")
                    r = mid - 1
                elif nums[r] < target and nums[mid] < target and nums[r] > nums[mid]:
                    print("5")
                    r = mid - 1
                elif nums[r] < target and nums[mid] < target and nums[r] < nums[mid]:
                    print("6")
                    l = mid + 1

        if nums[mid] == target:
            return mid
        else:
            return -1
        
if __name__ == "__main__":
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0)) #4
    print(s.search([4,5,6,7,0,1,2], 3)) #-1
    print(s.search([1], 0)) #-1