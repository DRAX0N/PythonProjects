"""
3105. Longest Strictly Increasing or Strictly Decreasing Subarray
Easy
Topics
premium lock icon
Companies
You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

 

Example 1:

Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.

Example 2:

Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.

Example 3:

Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.

 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50
"""
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        st = 0
        cnt = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if st == 1:
                    cnt += 1
                else:
                    res = max(res, cnt)
                    st = 1
                    cnt = 2
            elif nums[i-1] < nums[i]:
                if st == 2:
                    cnt += 1
                else:
                    res = max(res, cnt)
                    st = 2
                    cnt = 2
            else:
                st = 0          
        res = max(res, cnt)
        return res

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec, ans = 1, 1, 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                inc += 1
                dec = 1
            elif nums[i-1] > nums[i]:
                dec += 1
                inc = 1
            else:
                dec = 1
                inc = 1
            ans = max(ans, dec, inc)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.longestMonotonicSubarray([1,4,3,3,2]))  # Output: 2
    print(s.longestMonotonicSubarray([3,3,3,3]))    # Output: 1
    print(s.longestMonotonicSubarray([3,2,1]))      # Output: 3