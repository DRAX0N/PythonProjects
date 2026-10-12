"""
3876. Construct Uniform Parity Array II
Medium
Topics
premium lock icon
Companies
Hint
You are given an array nums1 of n distinct integers.

You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.

For each index i, you must choose exactly one of the following (in any order):

nums2[i] = nums1[i]​​​​​​​
nums2[i] = nums1[i] - nums1[j], for an index j != i, such that nums1[i] - nums1[j] >= 1
Return true if it is possible to construct such an array, otherwise return false.

 

Example 1:

Input: nums1 = [1,4,7]

Output: true

Explanation:​​​​​​​​​​​​​​

Set nums2[0] = nums1[0] = 1.
Set nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3.
Set nums2[2] = nums1[2] = 7.
nums2 = [1, 3, 7], and all elements are odd. Thus, the answer is true.
Example 2:

Input: nums1 = [2,3]

Output: false

Explanation:

It is not possible to construct nums2 such that all elements have the same parity. Thus, the answer is false.

Example 3:

Input: nums1 = [4,6]

Output: true

Explanation:

Set nums2[0] = nums1[0] = 4.
Set nums2[1] = nums1[1] = 6.
nums2 = [4, 6], and all elements are even. Thus, the answer is true.
 

Constraints:

1 <= n == nums1.length <= 105
1 <= nums1[i] <= 109
nums1 consists of distinct integers.
"""

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        def check_even_odd(num):
            res = 0
            if num[0]%2==0:
                res = 2
            else:
                res = 1
            for n in num[1:]:
                if n%2 == 0 and res == 2:
                    continue
                elif n%2 == 1 and res == 1:
                    continue
                else:
                    return False
            return True

        if check_even_odd(nums1):
            return True

        diff = [nums1[i]-nums1[i-1] for i in range(1,len(nums1))]

        if 1 not in diff:
            return True
        else:
            return False


class Solution:
    def uniformArray(self, a):
        mn = float('inf')
        oddCnt = 0
        for x in a:
            mn = min(mn, x)
            if x % 2 == 1:
                oddCnt += 1
        # min Element is ODD(remaining even > min) or All Even!
        return mn % 2 == 1 or oddCnt == 0
    
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        m=min(nums1)
        if m&1:
            return True
        for n in nums1:
            if n&1:
                return False
        return True  
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.uniformArray([1, 4, 7]))  # Output: True
    print(solution.uniformArray([2, 3]))     # Output: False
    print(solution.uniformArray([4, 6]))     # Output: True