"""
2540. Minimum Common Value
Easy
Topics
premium lock icon
Companies
Hint
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.
Example 2:

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
Both nums1 and nums2 are sorted in non-decreasing order.
"""

from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        res = float("infinity")
        if len(nums1) > len(nums2):
            for n in nums2:
                if n in nums1:
                    res = min(res,n)
        else:
            for n in nums1:
                if n in nums2:
                    res = min(res,n)
        
        if res == float("infinity"):
            return -1
        else:
            return res
        
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        res = float("infinity")
        l1 = len(nums1)
        l2 = len(nums2)

        i, j = 0, 0
        while True:
            if nums1[i] == nums2[j]:
                res = min(res, nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
            
            if i == l1 or j == l2:
                break

        if res == float("infinity"):
            return -1
        else:
            return res

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)

        i, j = 0, 0
        while True:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
            
            if i == l1 or j == l2:
                break

        return -1

        

if __name__ == "__main__":
    s = Solution()
    print(s.getCommon([1,2,3], [2,4])) # 2
    print(s.getCommon([1,2,3,6], [2,3,4,5])) # 2