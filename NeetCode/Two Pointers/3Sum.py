"""
3Sum
Medium
Topics
Company Tags
Hints
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
"""

#class Solution:
#    def threeSum(self, nums: List[int]) -> List[List[int]]:
#        nums.sort()
#        left, right = 0, len(nums)-1
#        result = []
#        while left<right:
#            print([nums[left], 0-nums[left]-nums[right], nums[right]])
#            if ((0-nums[left]-nums[right]) in nums[left+1:right]) or ((0-nums[left]-nums[right]) in nums[right+1:]) or ((0-nums[left]-nums[right]) in nums[:left]):
#                print("IM IN")
#                temp = [nums[left], 0-nums[left]-nums[right], nums[right]]
#                temp.sort()
#                if temp not in result:
#                    result.append(temp)
#                left += 1
#            elif 0-nums[left]-nums[right]<=0:
#                left += 1
#            #elif 0-nums[left]-nums[right]>0:
#            else:
#                right -= 1
#        print("ANWSER")
#        return result class Solution:


# slow solution
#class Solution:
#    def threeSum(self, nums: List[int]) -> List[List[int]]:
#        nums.sort()
#        print(nums)
#        #left, right = 0, len(nums)-1
#        result = []
#        for index, number in enumerate(nums):
#            left = index +1
#            right = len(nums)-1
#            while left<right:
#                #print([number, nums[left], nums[right]])
#                if (number + nums[left] + nums[right]) == 0:
#                    #print("IM IN")
#                    temp = [number, nums[left], nums[right]]
#                    if temp not in result:
#                        result.append(temp)
#                    left += 1
#                elif (number + nums[left] + nums[right]) < 0:
#                    left += 1
#                #elif 0-nums[left]-nums[right]>0:
#                else:
#                    right -= 1
#        return result     

# solution 3
#class Solution:
#    def threeSum(self, nums: list[int]) -> list[list[int]]:
#        nums.sort()
#        result = []
#        for index in range(len(nums)-2):
#            if index > 0 and nums[index] == nums[index - 1]: 
#                continue
#            left = index +1
#            right = len(nums)-1
#            while left<right:
#                total = nums[index] + nums[left] + nums[right]
#                if total == 0:
#                    temp = [nums[index], nums[left], nums[right]]
#                    #if temp not in result:
#                    result.append(temp)
#                    left += 1
#                elif total < 0:
#                    oldnum = nums[left]
#                    while oldnum == nums[left] and left>0 and left<right:
#                        left += 1
#                #elif 0-nums[left]-nums[right]>0:
#                else:
#                    oldnum = nums[right]
#                    while oldnum == nums[right] and right>0 and left<right:
#                        right -= 1
#        anwser = set(tuple(triplet) for triplet in result)
#        return [list(triplet) for triplet in anwser]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # O(n log n) – już masz!
        result = []
        n = len(nums)
        
        # Zmiana 1: for TYLKO do n-2, skip duplikatów FIXED i
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplikatów i
                continue
            
            # Zmiana 2: left = i+1, NIE index+1
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # Znaleziono triplet!
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Zmiana 3: SKIP duplikatów left/right – kluczowe!
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1  # Twój kod ✓
                else:
                    right -= 1  # Twój kod ✓
        
        return result

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    nums=[-1,0,1,2,-1,-4,-2,-3,3,0,4]
    nums = [1,1,1]
    #nums.sort()
    #print(nums)
    #nums.index()
    new = Solution()
    print(new.threeSum(nums)) #expected [[-1,-1,2],[-1,0,1]]