"""
3737. Count Subarrays With Majority Element I
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and an integer target.

Return the number of subarrays of nums in which target is the majority element.

The majority element of a subarray is the element that appears strictly more than half of the times in that subarray.

 

Example 1:

Input: nums = [1,2,2,3], target = 2

Output: 5

Explanation:

Valid subarrays with target = 2 as the majority element:

nums[1..1] = [2]
nums[2..2] = [2]
nums[1..2] = [2,2]
nums[0..2] = [1,2,2]
nums[1..3] = [2,2,3]
So there are 5 such subarrays.

Example 2:

Input: nums = [1,1,1,1], target = 1

Output: 10

Explanation:

​​​​​​​All 10 subarrays have 1 as the majority element.

Example 3:

Input: nums = [1,2,3], target = 4

Output: 0

Explanation:

target = 4 does not appear in nums at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.

 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 10​​​​​​​9
1 <= target <= 109
"""

from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] == target:
                    cnt += 1
                if cnt * 2 > (j - i + 1):
                    ans += 1

        return ans
    
from typing import List

class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        n = self.n
        bit = self.bit
        while i <= n:
            bit[i] += delta
            i += i & -i

    def sum(self, i: int) -> int:
        s = 0
        bit = self.bit
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pref = 0
        vals = [0]

        for x in nums:
            pref += 1 if x == target else -1
            vals.append(pref)

        uniq = sorted(set(vals))
        pos = {v: i + 1 for i, v in enumerate(uniq)}

        fw = Fenwick(len(uniq))
        ans = 0

        fw.add(pos[0], 1)

        pref = 0
        for x in nums:
            pref += 1 if x == target else -1
            idx = pos[pref]
            ans += fw.sum(idx - 1)
            fw.add(idx, 1)

        return ans
    
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        t = target
        cnt = [0] * (n*2+2)
        acc = [0] * (n*2+2)
        pre = n+1
        cnt[pre]=1
        acc[pre]=1
        res =0
        for num in nums:
            if t==num:
                pre+=1
            else:
                pre-=1
            cnt[pre]+=1
            acc[pre] = acc[pre-1] + cnt[pre]
            res+=acc[pre-1]
        return res
    
if __name__ == "__main__":
    print(Solution().countMajoritySubarrays([1,2,2,3], 2)) #5
    print(Solution().countMajoritySubarrays([1,1,1,1], 1)) #10
    print(Solution().countMajoritySubarrays([1,2,3], 4)) #0
