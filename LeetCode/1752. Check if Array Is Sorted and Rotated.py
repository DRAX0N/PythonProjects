"""
1752. Check if Array Is Sorted and Rotated
Easy
Topics
premium lock icon
Companies
Hint
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""


from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        temp = nums + nums
        t_res = 1
        res = 0
        n = len(temp)
        i=1
        while i <= n-1:
            if temp[i]>=temp[i-1]:
                t_res += 1
            else:
                t_res = 1
            res = max(res, t_res)
            i += 1
        return res >= len(nums)
    
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        return count <= 1     

if __name__ == "__main__":
    s = Solution()
    print(s.check([3,4,5,1,2])) # True
    print(s.check([2,1,3,4])) # False
    print(s.check([1,2,3])) # True
    print(s.check([1,1,1])) # True
