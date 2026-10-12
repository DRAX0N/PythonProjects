"""
2333. Minimum Sum of Squared Difference
Medium
Topics
premium lock icon
Companies
Hint
You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.

You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.

Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

Note: You are allowed to modify the array elements to become negative integers.

 

Example 1:

Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
Output: 579
Explanation: The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0. 
The sum of square difference will be: (1 - 2)2 + (2 - 10)2 + (3 - 20)2 + (4 - 19)2 = 579.
Example 2:

Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
Output: 43
Explanation: One way to obtain the minimum sum of square difference is: 
- Increase nums1[0] once.
- Increase nums2[2] once.
The minimum of the sum of square difference will be: 
(2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43.
Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.
 

Constraints:

n == nums1.length == nums2.length
1 <= n <= 105
0 <= nums1[i], nums2[i] <= 105
0 <= k1, k2 <= 109
"""
from collections import Counter
import heapq

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Calculate the absolute differences
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_k = k1 + k2

        # Use a max heap to always reduce the largest difference
        max_heap = [-d for d in diffs if d > 0]  # Only consider positive differences
        heapq.heapify(max_heap)

        while total_k > 0 and max_heap:
            largest_diff = -heapq.heappop(max_heap)
            if largest_diff == 0:
                break
            
            # Reduce the largest difference by 1
            largest_diff -= 1
            total_k -= 1
            
            # Push the reduced difference back into the heap if it's still positive
            if largest_diff > 0:
                heapq.heappush(max_heap, -largest_diff)

        # Calculate the sum of squared differences
        return sum(d * d for d in [-d for d in max_heap])
    
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        d = [0] * 100001
        k = k1 + k2
        total = 0
        mx = 0

        # Step 1: count the differences
        for a, b in zip(nums1, nums2):
            x = abs(a - b)
            d[x] += 1
            total += x
            mx = max(mx, x)

        # Enough budget -> every difference becomes 0
        if total <= k:
            return 0

        # Step 2: shave the biggest differences, level by level
        for i in range(mx, 0, -1):
            if k <= 0:
                break
            move = min(k, d[i])
            d[i] -= move
            d[i - 1] += move
            k -= move

        # Step 3: add up the squares
        ans = 0
        for i in range(mx + 1):
            ans += i * i * d[i]

        return ans

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 4]
    nums2 = [2, 10, 20, 19]
    k1 = 0
    k2 = 0
    print(solution.minSumSquareDiff(nums1, nums2, k1, k2))  # Output: 579

    nums1 = [1, 4, 10, 12]
    nums2 = [5, 8, 6, 9]
    k1 = 1
    k2 = 1
    print(solution.minSumSquareDiff(nums1, nums2, k1, k2))  # Output: 43