"""
3689. Maximum Total Subarray Value I
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of length n and an integer k.

You need to choose exactly k non-empty subarrays nums[l..r] of nums. Subarrays may overlap, and the exact same subarray (same l and r) can be chosen more than once.

The value of a subarray nums[l..r] is defined as: max(nums[l..r]) - min(nums[l..r]).

The total value is the sum of the values of all chosen subarrays.

Return the maximum possible total value you can achieve.

 

Example 1:

Input: nums = [1,3,2], k = 2

Output: 4

Explanation:

One optimal approach is:

Choose nums[0..1] = [1, 3]. The maximum is 3 and the minimum is 1, giving a value of 3 - 1 = 2.
Choose nums[0..2] = [1, 3, 2]. The maximum is still 3 and the minimum is still 1, so the value is also 3 - 1 = 2.
Adding these gives 2 + 2 = 4.

Example 2:

Input: nums = [4,2,5,1], k = 3

Output: 12

Explanation:

One optimal approach is:

Choose nums[0..3] = [4, 2, 5, 1]. The maximum is 5 and the minimum is 1, giving a value of 5 - 1 = 4.
Choose nums[0..3] = [4, 2, 5, 1]. The maximum is 5 and the minimum is 1, so the value is also 4.
Choose nums[2..3] = [5, 1]. The maximum is 5 and the minimum is 1, so the value is again 4.
Adding these gives 4 + 4 + 4 = 12.

 

Constraints:

1 <= n == nums.length <= 5 * 10​​​​​​​4
0 <= nums[i] <= 109
1 <= k <= 105
"""
#Hint 1
#For fixed l, the sequence v(l,r)=max(nums[l..r])−min(nums[l..r]) is non-increasing as r moves left.
#Hint 2
#Build RMQs (sparse tables) for range max/min so each v(l,r) is queryable in O(1).
#Hint 3
#Use a max-heap with v(l,n-1) for all l; pop the largest k times, and after popping an entry from (l,r) push (l,r-1) if r>l.

from typing import List
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        log = n.bit_length()
        st_max = [[0] * n for _ in range(log)]
        st_min = [[0] * n for _ in range(log)]
        for i in range(n):
            st_max[0][i] = nums[i]
            st_min[0][i] = nums[i]
        for j in range(1, log):
            for i in range(n - (1 << j) + 1):
                st_max[j][i] = max(st_max[j-1][i], st_max[j-1][i + (1 << (j-1))])
                st_min[j][i] = min(st_min[j-1][i], st_min[j-1][i + (1 << (j-1))])
        
        def query(l, r):
            length = r - l + 1
            j = length.bit_length() - 1
            max_val = max(st_max[j][l], st_max[j][r - (1 << j) + 1])
            min_val = min(st_min[j][l], st_min[j][r - (1 << j) + 1])
            return max_val - min_val
        
        heap = []
        for l in range(n):
            heapq.heappush(heap, (-query(l, n-1), l, n-1))
        total_value = 0
        for _ in range(k):
            value, l, r = heapq.heappop(heap)
            total_value -= value
            if r > l:
                heapq.heappush(heap, (-query(l, r-1), l, r-1))
        return total_value

if __name__ == "__main__":
    s = Solution()
    print(s.maxTotalValue([1,3,2], 2))  # Output: 4
    print(s.maxTotalValue([4,2,5,1], 3))  # Output: 12
    print(s.maxTotalValue([11,8], 2))  # Output: 3
    print(s.maxTotalValue([9,9,37], 3))  # Output: 56