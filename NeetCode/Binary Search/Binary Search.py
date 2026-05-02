"""
Binary Search
Easy
Topics
Company Tags
Hints
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in 
O
(
l
o
g
n
)
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.
"""

# slow solution
#class Solution:
#    def search(self, nums: List[int], target: int) -> int:
#        for i, n in enumerate(nums):
#            if n == target:
#                return i
#        return -1


# 2nd solution
#class Solution:
#    def search(self, nums: List[int], target: int) -> int:
#        if target in nums:
#            return nums.index(target)
#        else:
#            return -1

# 3rd solution   
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if(target==nums[mid]):
              return mid
            elif(target<nums[mid]):
               high=mid-1
            else:
              low=mid+1
        return -1
if __name__ == '__main__':
    nums = [-1,0,2,4,6,8]
    target = 4              # output 3
    #nums = [-1,0,2,4,6,8] 
    #target = 3              # output -1
    new = Solution()
    print(new.search(nums, target)) #