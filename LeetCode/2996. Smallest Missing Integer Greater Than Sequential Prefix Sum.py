"""
2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed array of integers nums.

A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.

Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.

 

Example 1:

Input: nums = [1,2,3,2,5]
Output: 6
Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
Example 2:

Input: nums = [3,4,5,1,12,14,13]
Output: 15
Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50
"""
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        cnt = 1
        suma = nums[0]
        res = []
        for i in range(len(nums)):
            if nums[i]-1 == nums[i-1]:
                suma += nums[i]
                cnt += 1
            else:
                res.append((cnt, suma))
                cnt = 1
                suma = nums[i]
        res.append((cnt, suma))
        res.sort()
        if res[-1][1] not in nums:
            return res[-1][1]
        else:
            j = res[-1][1]
            while j in nums:
                j += 1
        return j
    
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        index = 1
        while index < len(nums) and nums[index] == nums[index - 1] + 1:
            prefix_sum += nums[index]
            index += 1
        present = set(nums)
        while prefix_sum in present:
            prefix_sum += 1
        return prefix_sum
    
if __name__ == "__main__":
    s = Solution()

    print(s.missingInteger([1,2,3,2,5])) #6

    print(s.missingInteger([3,4,5,1,12,14,13])) #15