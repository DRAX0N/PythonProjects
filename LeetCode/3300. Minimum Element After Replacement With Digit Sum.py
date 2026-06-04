"""
3300. Minimum Element After Replacement With Digit Sum
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.

 

Example 1:

Input: nums = [10,12,13,14]

Output: 1

Explanation:

nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

Example 2:

Input: nums = [1,2,3,4]

Output: 1

Explanation:

nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.

Example 3:

Input: nums = [999,19,199]

Output: 10

Explanation:

nums becomes [27, 10, 19] after all replacements, with minimum element 10.

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 104
"""

from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        def numSum(number):
            res = 0
            for n in str(number):
                res += int(n)
            return res
        
        res = float("inf")
        for n in nums:
            if n > 9:
                res = min(res, numSum(n))
            else:
                res = min(res, n)
        return res
    
class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        min_res = float('inf')

        for n in nums:
            cur = 0
            while n:
                cur += n % 10
                n //= 10
            min_res = min(min_res, int(cur))
        return min_res
    
if __name__ == "__main__":
    s = Solution() 
    print(s.minElement([10,12,13,14])) # 1
    print(s.minElement([1,2,3,4])) # 1
    print(s.minElement([999,19,199])) # 10