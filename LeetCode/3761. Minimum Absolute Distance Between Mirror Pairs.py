"""
3761. Minimum Absolute Distance Between Mirror Pairs
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

A mirror pair is a pair of indices (i, j) such that:

0 <= i < j < nums.length, and
reverse(nums[i]) == nums[j], where reverse(x) denotes the integer formed by reversing the digits of x. Leading zeros are omitted after reversing, for example reverse(120) = 21.
Return the minimum absolute distance between the indices of any mirror pair. The absolute distance between indices i and j is abs(i - j).

If no mirror pair exists, return -1.

 

Example 1:

Input: nums = [12,21,45,33,54]

Output: 1

Explanation:

The mirror pairs are:

(0, 1) since reverse(nums[0]) = reverse(12) = 21 = nums[1], giving an absolute distance abs(0 - 1) = 1.
(2, 4) since reverse(nums[2]) = reverse(45) = 54 = nums[4], giving an absolute distance abs(2 - 4) = 2.
The minimum absolute distance among all pairs is 1.

Example 2:

Input: nums = [120,21]

Output: 1

Explanation:

There is only one mirror pair (0, 1) since reverse(nums[0]) = reverse(120) = 21 = nums[1].

The minimum absolute distance is 1.

Example 3:

Input: nums = [21,120]

Output: -1

Explanation:

There are no mirror pairs in the array.

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109​​​​​​​
"""
from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        #expected output code below should achieve is in comment where function is called
        def reverse(x: int) -> int:
            return int(str(x)[::-1])
        n = len(nums)
        res = float("inf")
        for i in range(n):
            for j in range(i + 1, n):
                if reverse(nums[i]) == nums[j]:
                    res = min(res, abs(i - j))
        return res if res != float("inf") else -1
    

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(x: int) -> int:
            return int(str(x)[::-1])

        pos = {}   # pos[rv] = OSTATNI indeks gdzie rev(nums[idx]) == rv
        ans = float("inf")

        for i, x in enumerate(nums):
            rx = rev(x)

            # Czy x jest prawą stroną pary? Ktoś wcześniej miał rev == x
            if x in pos:
                ans = min(ans, i - pos[x])

            # Zapisz pod kluczem rx - ZAWSZE nadpisuj najnowszym indeksem!
            pos[rx] = i   # ← zmiana z `if rx not in pos` na bezwarunkowe

        return -1 if ans == float("inf") else ans
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.minMirrorPairDistance([12,21,45,33,54])) # expected output: 1
    print(solution.minMirrorPairDistance([120,21])) # expected output: 1
    print(solution.minMirrorPairDistance([21,120])) # expected output: -1