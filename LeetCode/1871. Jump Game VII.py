"""
1871. Jump Game VII
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
 

Constraints:

2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length

# Consider for each reachable index i the interval [i + a, i + b].
# Use partial sums to mark the intervals as reachable.
"""

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        reachable = [0] * n
        reachable[0] = 1
        prefix_sum = 0

        for i in range(minJump, n):
            prefix_sum += reachable[i - minJump]
            if i > maxJump:
                prefix_sum -= reachable[i - maxJump - 1]

            if prefix_sum > 0 and s[i] == '0':
                reachable[i] = 1

        return reachable[-1] == 1

if __name__ == "__main__":
    s = Solution()
    print(s.canReach("011010", 2, 3)) # True
    print(s.canReach("01101110", 2, 3)) # False