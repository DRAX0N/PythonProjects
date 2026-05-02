"""
Top K Frequent Elements
Medium
Topics
Company Tags
Hints
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(set(nums)) < k:
            return list(set(nums))
        elif len(nums) == 1:
            return nums
        
        counter = {}
        for number in nums:
            if number in counter:
                counter[number] += 1
            else:
                counter[number] = 1

        values = list(counter.values())
        keys = list(counter.keys())
        result = []
        for i in range(k):
            max_index = -1
            max_value = max(values)
            max_index = values.index(max_value)
            result.append(keys[max_index])
            values.remove(values[max_index])
            keys.remove(keys[max_index])
        return result

nums = [1,2,2,3,3,3,4]
k = 2
new = Solution()
solution = new.topKFrequent(nums, k)
print(solution)
