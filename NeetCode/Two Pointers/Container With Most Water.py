"""
Container With Most Water
Medium
Topics
Company Tags
Hints
You are given an integer array heights where heights[i] represents the height of the 
i
t
h
i 
th
  bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:



Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000
"""
# solution slow
#class Solution:
#    def maxArea(self, heights: List[int]) -> int:
#        maxField = 0
#        l, r = 0, len(heights)-1
#        maxheight = max(heights)
#        h = 0
#        for index in range(heights.index(maxheight)+1):
#            l, r = index, len(heights)-1
#            while l<r:
#                if heights[l]>heights[r]:
#                    h = heights[r]
#                else:
#                    h = heights[l]
#                w = r-l
#                if h*w>maxField:
#                    maxField = h*w
#                r -= 1
#        return maxField
    
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxField = 0
        l, r = 0, len(heights)-1
        h = 0
        while l<r:
            if heights[l]>heights[r]:
                h = heights[r]
            else:
                h = heights[l]
            w = r-l
            if h*w>maxField:
                maxField = h*w

            if heights[l]>heights[r]:
                r -= 1
            else:
                l += 1    
        return maxField
        
        

if __name__ == '__main__':
    #height = [1,7,2,5,4,7,3,6] #expected 36
    #height = [2,2,2] #expected 4
    #height=[1,7,2,5,12,3,500,500,7,8,4,7,3,6] #500
    height=[1,7,1,1,1,1,2,5,12,3,500,50,7,8,4,7,38,9,10,12,6] #228
    new = Solution()
    print(new.maxArea(height)) #