"""
2784. Check if Array is Good
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].

base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].

Return true if the given array is good, otherwise return false.

Note: A permutation of integers represents an arrangement of these numbers.

 

Example 1:

Input: nums = [2, 1, 3]
Output: false
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. However, base[3] has four elements but array nums has three. Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.
Example 2:

Input: nums = [1, 3, 3, 2]
Output: true
Explanation: Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. It can be seen that nums is a permutation of base[3] = [1, 2, 3, 3] (by swapping the second and fourth elements in nums, we reach base[3]). Therefore, the answer is true.
Example 3:

Input: nums = [1, 1]
Output: true
Explanation: Since the maximum element of the array is 1, the only candidate n for which this array could be a permutation of base[n], is n = 1. It can be seen that nums is a permutation of base[1] = [1, 1]. Therefore, the answer is true.
Example 4:

Input: nums = [3, 4, 4, 1, 2, 1]
Output: false
Explanation: Since the maximum element of the array is 4, the only candidate n for which this array could be a permutation of base[n], is n = 4. However, base[4] has five elements but array nums has six. Therefore, it can not be a permutation of base[4] = [1, 2, 3, 4, 4]. So the answer is false.
 

Constraints:

1 <= nums.length <= 100
1 <= num[i] <= 200
"""

from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        lenght = len(nums)
        if lenght < 2:
            return False
        elif nums[-1] == nums[-2]:
            i = 1
            for n in nums[0:lenght-1]:
                if n == i:
                    i += 1
                else:
                    return False
            return True
        else:
            return False
        
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()

        max_ele = nums[-1]
        if len(nums) != max_ele + 1 or nums[-1] != nums[-1-1]:
            return False
        
        for i in range(max_ele - 1):
            if nums[i] != i + 1:
                return False
        return True
    
if __name__ == "__main__":
    s = Solution()
    print(s.isGood([2, 1, 3])) # False
    print(s.isGood([1, 3, 3, 2])) # True
    print(s.isGood([1, 1])) # True
    print(s.isGood([3, 4, 4, 1, 2, 1])) # False
    print(s.isGood([9, 9])) # False
