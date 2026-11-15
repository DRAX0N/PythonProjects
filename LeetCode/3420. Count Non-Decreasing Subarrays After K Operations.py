"""
3420. Count Non-Decreasing Subarrays After K Operations
Hard
Topics
premium lock icon
Companies
Hint
You are given an array nums of n integers and an integer k.

For each subarray of nums, you can apply up to k operations on it. In each operation, you increment any element of the subarray by 1.

Note that each subarray is considered independently, meaning changes made to one subarray do not persist to another.

Return the number of subarrays that you can make non-decreasing ​​​​​after performing at most k operations.

An array is said to be non-decreasing if each element is greater than or equal to its previous element, if it exists.

 

Example 1:

Input: nums = [6,3,1,2,4,4], k = 7

Output: 17

Explanation:

Out of all 21 possible subarrays of nums, only the subarrays [6, 3, 1], [6, 3, 1, 2], [6, 3, 1, 2, 4] and [6, 3, 1, 2, 4, 4] cannot be made non-decreasing after applying up to k = 7 operations. Thus, the number of non-decreasing subarrays is 21 - 4 = 17.

Example 2:

Input: nums = [6,3,1,3,6], k = 4

Output: 12

Explanation:

The subarray [3, 1, 3, 6] along with all subarrays of nums with three or fewer elements, except [6, 3, 1], can be made non-decreasing after k operations. There are 5 subarrays of a single element, 4 subarrays of two elements, and 2 subarrays of three elements except [6, 3, 1], so there are 1 + 5 + 4 + 2 = 12 subarrays that can be made non-decreasing.

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        result = cost = 0
        dq = deque()              # indeksy, wartości nums malejące
        right = len(nums) - 1
        for left in range(len(nums) - 1, -1, -1):
            while dq and nums[dq[-1]] < nums[left]:
                l = dq.pop()
                r = dq[-1] - 1 if dq else right
                cost += (r - l + 1) * (nums[left] - nums[l])
            dq.append(left)
            while cost > k:
                cost -= nums[dq[0]] - nums[right]
                if dq[0] == right:
                    dq.popleft()
                right -= 1
            result += right - left + 1
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.countNonDecreasingSubarrays([6,3,1,2,4,4], 7))  # Output: 17
    print(s.countNonDecreasingSubarrays([6,3,1,3,6], 4))  # Output: 12