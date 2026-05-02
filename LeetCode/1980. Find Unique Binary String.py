"""
1980. Find Unique Binary String
Medium
Topics
premium lock icon
Companies
Hint
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 

Constraints:

n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
"""

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_len = len(nums)
        n_len = len(nums[0])
        int_list = [int(n, 2) for n in nums]
        int_list.sort()
        ans = ""
        for n in range(2**n_len):
            if n not in int_list:
                if len(bin(n)[2:]) < n_len:
                    ans = "0"*(n_len - len(bin(n)[2:])) + str(bin(n)[2:])
                    return ans
                else:
                    return str(bin(n)[2:])

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l=[]
        for i in range(len(nums)):
            if nums[i][i]=='0':
                l.append('1')
            else:
                l.append('0')
        return ''.join(l)

if __name__ == '__main__':
    nums = ["01","10"] #"11"
    nums = ["00","01"] # "11"
    nums = ["111","011","001", "000"] #"000", "010", "100"
    # 000 001 010 100 011 110 101 111 2**3
    new = Solution()
    print(new.findDifferentBinaryString(nums))