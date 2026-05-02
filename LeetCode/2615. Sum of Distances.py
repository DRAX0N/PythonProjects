"""
2615. Sum of Distances
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

Return the array arr.

 

Example 1:

Input: nums = [1,3,1,1,2]
Output: [5,0,3,4,0]
Explanation: 
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
When i = 4, arr[4] = 0 because there is no other index with value 2. 

Example 2:

Input: nums = [0,5,3]
Output: [0,0,0]
Explanation: Since each element in nums is distinct, arr[i] = 0 for all i.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
"""

from collections import defaultdict
from operator import setitem
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        d = defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
        res = [0] * len(nums)
        for k, v in d.items():
            if len(v) == 1:
                continue
            prefix_sum = [0] * len(v)
            prefix_sum[0] = v[0]
            for i in range(1, len(v)):
                prefix_sum[i] = prefix_sum[i-1] + v[i]
            for i in range(len(v)):
                left_sum = prefix_sum[i-1] if i > 0 else 0
                right_sum = prefix_sum[-1] - prefix_sum[i]
                res[v[i]] = (i * v[i] - left_sum) + (right_sum - (len(v)-i-1) * v[i])
        return res
    
def distance(self, nums: List[int]) -> List[int]:
        n_len = len(nums)
        result = [0]*n_len
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if n == m and i != j:
                    result[i] += abs(i-j)
        return result
    
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n_len = len(nums)
        result = [0]*n_len
        num_dict = {}
        for i, n in enumerate(nums):
            if n not in num_dict:
                num_dict[n] = []
            num_dict[n].append(i)
        
        for n, indices in num_dict.items():
            for i in indices:
                for j in indices:
                    if i != j:
                        result[i] += abs(i-j)
        
        return result

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # for a certain x the 'i's are
        # [i0, i1, ... , ik, ..., i(n-1) ]
        # for ik SoD is (
        #    ik*k - SUM([i0..i(k-1)])
        #    + SUM([i(k+1)..i(n-1)]) - ik*(n-1-k)
        # ) = ik*(2k-n+1) - PSi[k] + PSi[n] - PSi[k + 1]
        ans = [0] * len(nums)
        indices_of_value = defaultdict(list)
        for i, num in enumerate(nums):
            indices_of_value[num].append(i)
        for indices in indices_of_value.values():
            n = len(indices)
            if n == 1:
                continue
            total = sum(indices)
            psk0, psk1 = 0, 0
            imul = -n - 1
            for k, idx in enumerate(indices):
                psk0, psk1 = psk1, psk0
                psk1 = psk0 + idx
                imul += 2
                ans[idx] = (
                    idx * imul + total - psk1 - psk0
                )
        return ans
    
class Solution:
    def distance(self, a: List[int]) -> List[int]:
        d={};[d.setdefault(c,[]).append(i)for i,c in enumerate(a)];[setitem(a,x,s-len(t)*x-2*(x*~i+(p:=p+x)))for t in d.values()if[s:=sum(t),p:=0]for i,x in enumerate(t)];return a
    
if __name__ == "__main__":
    s = Solution()
    print(s.distance([1,3,1,1,2]))  # [5,0,3,4,0]
    print(s.distance([0,5,3]))  # [0,0,0]