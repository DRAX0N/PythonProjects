"""
Trapping Rain Water
Hard
Topics
Company Tags
Hints
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:



Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
Constraints:

1 <= height.length <= 1000
0 <= height[i] <= 1000
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        print(height)
        max_l = 0
        max_r = 0
        l, r = 0, len(height) - 1
        heighset_bar = max(height)
        temp_maxarea = heighset_bar*len(height)
        bars_area = sum(height)
        temp_maxarea -= bars_area
        print("before loop: " + str(temp_maxarea))
        while l<r and (height[l] < heighset_bar or height[r]<heighset_bar):
            if height[l]<heighset_bar:
                if height[l]> max_l:
                    max_l = height[l]
                #print("l: " + str(height[l]))
                temp_maxarea -= (heighset_bar-max_l)
                l+=1
            if height[r]<heighset_bar:
                if height[r]> max_r:
                    max_r = height[r]
                #print("r: " + str(height[r]))
                temp_maxarea -= (heighset_bar-max_r)
                r-=1

        return temp_maxarea


if __name__ == '__main__':
    height = [0,2,0,3,1,0,1,3,2,1] #9
    height =[4,2,0,3,2,5]
    new = Solution()
    print(new.trap(height))