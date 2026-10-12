"""
1621. Number of Sets of K Non-Overlapping Line Segments
Medium
Topics
premium lock icon
Companies
Hint
Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.

Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 109 + 7.

 

Example 1:


Input: n = 4, k = 2
Output: 5
Explanation: The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.
Example 2:

Input: n = 3, k = 1
Output: 3
Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.
Example 3:

Input: n = 30, k = 7
Output: 796297179
Explanation: The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 109 + 7 gives us 796297179.
 

Constraints:

2 <= n <= 1000
1 <= k <= n-1
"""

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        result = 1

        for i in range(1, 2 * k + 1):
            result = result * (n + k - i) % MOD
            result = result * pow(i, MOD - 2, MOD) % MOD

        return result

import math    
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # g0 + s0 + g1 + s1 + g2  => k+1 g's and k s's 
        # all gaps sum to n-1 i.e g0 + s0 + g1 + s1 + g2 = n-1 where s >= 1 and g >= 0
        # g0 + s0' + g1 + s1' + g2 = n-1 where s' >= 0
        # g0 + s0 + g1 + s1 + g2 = n-1-k here k =2
        # now total elements on left = k + k+1 = 2k+1
        # applying formula n+k-1 C k-1 here we get => n-1-k + 2k+1 - 1 C 2k+1 -1 = n + k - 1 C 2k 
        return math.comb(n+k-1,2*k)%(10**9+7)
    
if __name__ == "__main__":
    solution = Solution()
    n = 4
    k = 2
    print(solution.numberOfSets(n, k))  # Output: 5

    n = 3
    k = 1
    print(solution.numberOfSets(n, k))  # Output: 3

    n = 30
    k = 7
    print(solution.numberOfSets(n, k))  # Output: 796297179