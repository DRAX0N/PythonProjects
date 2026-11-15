"""
3886. Sum of Sortable Integers
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of length n.

An integer k is called sortable if k divides n and you can sort nums in non-decreasing order by sequentially performing the following operations:

Partition nums into consecutive subarrays of length k.
Cyclically rotate each subarray independently any number of times to the left or to the right.
Return an integer denoting the sum of all possible sortable integers k.

 

Example 1:

Input: nums = [3,1,2]

Output: 3

Explanation:​​​​​​​

For n = 3, possible divisors are 1 and 3.
For k = 1: each subarray has one element. No rotation can sort the array.
For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.
Only k = 3 is sortable. Hence, the answer is 3.
Example 2:

Input: nums = [7,6,5]

Output: 0

Explanation:

For n = 3, possible divisors are 1 and 3.
For k = 1: each subarray has one element. No rotation can sort the array.
For k = 3: the single subarray [7, 6, 5] cannot be rotated into non-decreasing order.
No k is sortable. Hence, the answer is 0.
Example 3:

Input: nums = [5,8]

Output: 3

Explanation:​​​​​​​

For n = 2, possible divisors are 1 and 2.
Since [5, 8] is already sorted, every divisor is sortable. Hence, the answer is 1 + 2 = 3.
 

Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= 105
"""

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0

        for k in range(1, n + 1):
            if n % k:
                continue

            prev_max = float("-inf")
            ok = True

            for start in range(0, n, k):
                block = nums[start:start + k]

                descents = 0
                for i in range(k):
                    if block[i] > block[(i + 1) % k]:
                        descents += 1
                        if descents > 1:
                            break
                if descents > 1:
                    ok = False
                    break

                if min(block) < prev_max:
                    ok = False
                    break
                prev_max = max(block)

            if ok:
                total += k

        return total
    
if __name__ == "__main__":
    nums = [3,1,2]
    print(Solution().sortableIntegers(nums))  # Output: 3
    nums = [7,6,5]
    print(Solution().sortableIntegers(nums))  # Output: 0
    nums = [5,8]
    print(Solution().sortableIntegers(nums))  # Output: 3
    nums = [12,18,14]
    print(Solution().sortableIntegers(nums))  # Output: 0
    nums = [2,3,4,1]
    print(Solution().sortableIntegers(nums))  # Output: 4