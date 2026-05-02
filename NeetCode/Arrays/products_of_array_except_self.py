"""
Products of Array Except Self
Medium
Topics
Company Tags
Hints
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20
"""

#class Solution:
#    def productExceptSelf(self, nums: List[int]) -> List[int]:
#        result = []
#        for i in range(len(nums)):
#            product = 1
#            for j, m in enumerate(nums):
#                if i != j:
#                    product *= m
#            result.append(product)
#        return result
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # prefix[i] = iloczyn ELEMTÓW PRZED i
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # suffix[i] = iloczyn ELEMTÓW PO i  
        suffix = [1] * n
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        # result[i] = prefix[i] * suffix[i]
        return [prefix[i] * suffix[i] for i in range(n)]

if __name__ == "__main__":
    nums = [-1,0,1,2,3]
    new = Solution()
    print(new.productExceptSelf(nums))