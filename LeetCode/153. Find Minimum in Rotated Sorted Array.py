"""
Find Minimum in Rotated Sorted Array
Medium
Topics
Company Tags
Hints
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2]

Output: 1
Example 2:

Input: nums = [4,5,0,1,2,3]

Output: 0
Example 3:

Input: nums = [4,5,6,7]

Output: 4
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
"""
# O(n) solution
#class Solution:
#    def findMin(self, nums: List[int]) -> int:
#        return min(nums)

# O(n) solution
#class Solution:
#    def findMin(self, nums: List[int]) -> int:
#        l, r = 0, len(nums)-1
#        result = nums[0]
#        while l<=r:
#            if nums[l] < nums[r]:
#                result = min(result, nums[l])
#                l +=1
#            else:
#                result = min(result, nums[r])
#                r -= 1
#        return result
    
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        print(nums)
        l, r = 0, len(nums)-1
        result = nums[0]
        while l<=r:
            mid = (l+r)//2
            #print("l: " + str(l))
            #print("r: " + str(r))
            if nums[l]> nums[mid] >=  nums[r]:
                l = mid
                result = min(result, nums[mid])
            elif nums[r]> nums[mid] >= nums[l]:
                r = mid
                result = min(result, nums[mid])
            elif nums[mid] < nums[l] and nums[mid] < nums[r]:
                r = mid - 1
                result = min(result, nums[mid])
            elif nums[r]>nums[l]:
                r -= 1
                result = min(result, nums[l])
            else:
                l += 1 
                result = min(result, nums[r])
     
        return result
if __name__ == '__main__':
    nums = [3,4,5,6,1,2] # output 1
    nums = [4,5,0,1,2,3] # output 0
    nums = [4,5,6,7]     # output 4
    nums=[5,1,2,3,4]     # output 1
    new = Solution()
    print(new.findMin(nums))