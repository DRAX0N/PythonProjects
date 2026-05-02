"""
Median of Two Sorted Arrays
Hard
Topics
Company Tags
Hints
You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

Your solution must run in 
O
(
l
o
g
(
m
+
n
)
)
O(log(m+n)) time.

Example 1:

Input: nums1 = [1,2], nums2 = [3]

Output: 2.0
Explanation: Among [1, 2, 3] the median is 2.

Example 2:

Input: nums1 = [1,3], nums2 = [2,4]

Output: 2.5
Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""
#O((m+n)log(m+n))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums)%2 == 1:
            return nums[(len(nums)+1)//2-1]
        else:
            n1_index = int((len(nums))/2-1)
            n2_index = int((len(nums)/2))
            return (nums[n2_index] + nums[n1_index])/2
        
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total//2

        if len(nums1)>len(nums2):
            a = nums2
            b = nums1
        else:
            a = nums1
            b = nums2
        
        l1, r1 = 0, len(a)-1
        while True:
            m1 = (l1 + r1) // 2  # shorter list
            m2 = half - m1 - 2

            a_left_side = a[m1] if m1>= 0 else float("-infinity")
            b_left_side = b[m2] if m2>= 0 else float("-infinity")
            a_right_side = a[m1 +1] if m1 +1 < len(a) else float("infinity")
            b_right_side = b[m2 +1] if m2 +1 < len(b) else float("infinity")

            if a_left_side <= b_right_side and b_left_side <= a_right_side:
                if total%2:
                    return min(a_right_side, b_right_side)
                else:
                    return (min(a_right_side, b_right_side) + max(a_left_side, b_left_side))/2
            else:

                if a_left_side > b_right_side:
                    r1 = m1 - 1
                else:
                    l1 = m1 + 1
        
if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [3]     #2.0
    nums1 = [1,3]
    nums2 = [2,4]   #2.5
    nums1=[0,0]
    nums2=[0,0]
    print(Solution().findMedianSortedArrays(nums1, nums2)) 