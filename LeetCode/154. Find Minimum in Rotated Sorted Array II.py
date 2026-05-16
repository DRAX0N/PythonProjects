"""
154. Find Minimum in Rotated Sorted Array II
Attempted
Hard
Topics
premium lock icon
Companies
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [1,3,5]
Output: 1
Example 2:

Input: nums = [2,2,2,0,1]
Output: 0
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        #print(nums)
        l, r = 0, len(nums)-1
        result = nums[0]
        while l<=r:
            mid = (l+r)//2
            #print("l: " + str(l))
            #print("r: " + str(r))
            if nums[l]> nums[mid] >  nums[r]:
                l = mid
                result = min(result, nums[mid])
            elif nums[l]> nums[mid] ==  nums[r]:
                r -= 1
                result = min(result, nums[l])
            elif nums[r]> nums[mid] > nums[l]:
                r = mid
                result = min(result, nums[mid])
            elif nums[r]> nums[mid] == nums[l]:
                l += 1
                result = min(result, nums[r])
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
    
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r = r - 1

        return nums[l]
    
if __name__ == "__main__":
    s = Solution()
    print(s.findMin([1,3,5])) # 1
    print(s.findMin([2,2,2,0,1])) # 0
    print(s.findMin([4,5,6,7])) # 4
    print(s.findMin([2,0,1,1,1])) # 0
    print(s.findMin([1,1,1,1,1])) # 1
    print(s.findMin([1,1,1,0,1])) # 0