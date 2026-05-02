"""
3740. Minimum Distance Between Three Equal Elements I
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].

The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.

Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

 

Example 1:

Input: nums = [1,2,1,1,3]

Output: 6

Explanation:

The minimum distance is achieved by the good tuple (0, 2, 3).

(0, 2, 3) is a good tuple because nums[0] == nums[2] == nums[3] == 1. Its distance is abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6.

Example 2:

Input: nums = [1,1,2,3,2,1,2]

Output: 8

Explanation:

The minimum distance is achieved by the good tuple (2, 4, 6).

(2, 4, 6) is a good tuple because nums[2] == nums[4] == nums[6] == 2. Its distance is abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8.

Example 3:

Input: nums = [1]

Output: -1

Explanation:

There are no good tuples. Therefore, the answer is -1.

 

Constraints:

1 <= n == nums.length <= 100
1 <= nums[i] <= n
"""
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        group = {}
        for i, n in enumerate(nums):
            if n in group.keys():
                group[n].append(i)
            else:
                group[n] = [i]
        res = float("infinity")
        for values in group.values():
            if len(values) == 3:
                res = min(res, (abs(values[0] - values[1]) + abs(values[1] - values[2]) + abs(values[2] - values[0])))
            elif len(values) > 3:
                for n in range(2,len(values)):
                    res = min(res, (abs(values[n-2] - values[n-1]) + abs(values[n-1] - values[n]) + abs(values[n] - values[n-2])))
            else:
                continue
        return -1 if res == float("infinity") else res
    
from collections import defaultdict
from math import inf

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        groups = defaultdict(list)
        for i, num in enumerate(nums):
            groups[num].append(i)
        least_half = inf
        for group in groups.values():
            if len(group) == 1:
                continue
            for i in range(2, len(group)):
                half = group[i] - group[i-2]
                if least_half > half:
                    least_half = half
        if least_half == inf:
            return -1
        return least_half << 1
    
if __name__ == "__main__":
    bravexuneth = Solution()
    print(bravexuneth.minimumDistance([1,2,1,1,3]))  # Output: 6
    print(bravexuneth.minimumDistance([1,1,2,3,2,1,2]))  # Output: 8
    print(bravexuneth.minimumDistance([1]))  # Output: -1
    print(bravexuneth.minimumDistance([2,2,3,2,2]))  # Output: 6