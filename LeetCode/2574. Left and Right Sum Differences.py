"""
2574. Left and Right Sum Differences
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums of size n.

Define two arrays leftSum and rightSum where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.

 

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 105
"""
from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        pre_sum = 0
        len_num = len(nums)
        post_sum = sum(nums)
        pre_array = [0]*len_num
        post_arry = [post_sum]*len_num
        for i in range(len_num):
            pre_array[i] = pre_sum
            pre_sum += nums[i]
            post_arry[i] -= pre_sum
        
        return [abs(pre_array[i] - post_arry[i]) for i in range(len_num)]

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        arr = []
        for i,cur_val in enumerate(nums):
            arr.append(abs(total_sum - left_sum - cur_val))
            left_sum += cur_val
            total_sum -= cur_val
        return arr

if __name__ == "__main__":
    s = Solution()
    print(s.leftRightDifference([10,4,8,3]))  # [15,1,11,22]
    print(s.leftRightDifference([1]))  # [0]