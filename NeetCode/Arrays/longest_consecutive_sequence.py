"""
Longest Consecutive Sequence
Medium
Topics
Company Tags
Hints
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        max_len = 1
        c_max_len = 1 
        nums.sort()
        curr = nums[0]
        for n in nums[1::]:
            if curr + 1 == n:
                c_max_len += 1
                curr = n
                if c_max_len > max_len:
                    max_len = c_max_len
            elif curr == n:
                pass
            else:
                c_max_len = 1 
                curr = n

        return max_len

if __name__ == "__main__":
    nums=[0,3,2,5,4,6,1,1]
    new = Solution()
    print(new.longestConsecutive(nums))