"""
Sliding Window Maximum
Hard
Topics
Company Tags
Hints
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.

Example 1:

Input: nums = [1,2,1,0,4,2,6], k = 3

Output: [2,2,4,4,6]

Explanation:
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6
Constraints:

1 <= nums.length <= 100,000
-10,000 <= nums[i] <= 10,000
1 <= k <= nums.length

"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 or k == 1:
            return nums
        l = 0
        r = l + k - 1
        max_list = []
        for l in range(len(nums) - k + 1):
            if r+1 <= len(nums):
                max_list.append(max(nums[l:r+1]))
            r += 1
        return max_list

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 or k == 1:
            return nums
        l = 0
        r = l + k - 1
        temp = nums[l:r+1]
        curr_max = max(temp)
        max_list = [curr_max]
        r += 1
        for l in range(1,len(nums) - k + 1):
            print(nums[l])
            print(nums[r])
            if r+1 <= len(nums):
                if nums[r]>curr_max:
                    curr_max = nums[r]
            if l < len(temp) and curr_max != nums[r]:
                if nums[l-1] == curr_max:
                    print("asfdasfd")
                    print("temp = " + str(temp[l:r+1]))
                    curr_max = max(temp[l:r+1])

            max_list.append(curr_max)
            print(max_list)
            r += 1
        return max_list
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = []
        l,r = 0,0
        while r < len(nums):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.pop(0)

            if r+1 >= k:
                ans.append(nums[q[0]])
                l+=1
            r+=1
        return ans


        
if __name__ == "__main__":
    s = Solution()
    #print(s.maxSlidingWindow([1,2,1,0,4,2,6], 3)) #expected [2,2,4,4,6]
    nums=[1,3,1,2,0,5]
    k=3
    print(s.maxSlidingWindow(nums, k))