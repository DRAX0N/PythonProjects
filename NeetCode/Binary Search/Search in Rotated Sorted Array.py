"""
Search in Rotated Sorted Array
Medium
Topics
Company Tags
Hints
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2], target = 1

Output: 4
Example 2:

Input: nums = [3,5,6,0,1,2], target = 4

Output: -1
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= target <= 1000
All values of nums are unique.
nums is an ascending array that is possibly rotated.

"""
# O(n) solution
#class Solution:
#    def search(self, nums: List[int], target: int) -> int:
#        return nums.index(target)

# O(logn) solution
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
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
     
if __name__ == '__main__':
    nums = [3,4,5,6,1,2]
    target = 1   # output 4

    nums = [3,5,6,0,1,2]
    target = 4   # output -1
#
    nums=[4,5,6,7,0,1,2]
    target = 0   # output 4
    #
    nums=[3,5,1]
    target=3    # output 0
#
    nums=[5,1,3]
    target=3    # output 2
    #
    #nums=[5,1,2,3,4]
    #target=1    # output 1
    nums=[3,1]
    target=4
    new = Solution()    
    print(new.search(nums, target))