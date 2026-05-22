"""
3043. Find the Length of the Longest Common Prefix
Medium
Topics
premium lock icon
Companies
Hint
You are given two arrays with positive integers arr1 and arr2.

A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. For example, 123 is a prefix of the integer 12345, while 234 is not.

A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. For example, 5655359 and 56554 have common prefixes 565 and 5655 while 1223 and 43456 do not have a common prefix.

You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs to arr1 and y belongs to arr2.

Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.

 

Example 1:

Input: arr1 = [1,10,100], arr2 = [1000]
Output: 3
Explanation: There are 3 pairs (arr1[i], arr2[j]):
- The longest common prefix of (1, 1000) is 1.
- The longest common prefix of (10, 1000) is 10.
- The longest common prefix of (100, 1000) is 100.
The longest common prefix is 100 with a length of 3.
Example 2:

Input: arr1 = [1,2,3], arr2 = [4,4,4]
Output: 0
Explanation: There exists no common prefix for any pair (arr1[i], arr2[j]), hence we return 0.
Note that common prefixes between elements of the same array do not count.
 

Constraints:

1 <= arr1.length, arr2.length <= 5 * 104
1 <= arr1[i], arr2[i] <= 108
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def common_prefix_length(a: int, b: int) -> int:
            a_str, b_str = str(a), str(b)
            i = 0
            while i < min(len(a_str), len(b_str)) and a_str[i] == b_str[i]:
                i += 1
            return i
        
        max_length = 0
        for x in arr1:
            for y in arr2:
                max_length = max(max_length, common_prefix_length(x, y))
        
        return max_length
    
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        #Put all the possible prefixes of each element in arr1 into a HashSet.
        #For all the possible prefixes of each element in arr2, check if it exists in the HashSet.
        prefix_set = set()
        for num in arr1:
            num_str = str(num)
            for i in range(1, len(num_str) + 1):
                prefix_set.add(num_str[:i])
        max_length = 0
        for num in arr2:
            num_str = str(num)
            for i in range(1, len(num_str) + 1):
                prefix = num_str[:i]
                if prefix in prefix_set:
                    max_length = max(max_length, i)
        return max_length

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix([1,10,100], [1000])) #3
    print(s.longestCommonPrefix([1,2,3], [4,4,4])) #0