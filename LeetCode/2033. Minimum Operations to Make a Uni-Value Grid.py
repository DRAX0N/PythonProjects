"""
2033. Minimum Operations to Make a Uni-Value Grid
Medium
Topics
premium lock icon
Companies
Hint
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

 

Example 1:


Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.
Example 2:


Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.
Example 3:


Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= x, grid[i][j] <= 104
"""

from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        one_list = [i for num  in grid for i in num]
        for num in one_list[1::]:
            if num%x != one_list[0]%x:
                return -1
        target = sum(one_list) // len(one_list)
        print(target)
        counter = 0
        #for index in range(len(one_list)):
        #    while True:
        #        if ((target-x) < one_list[index] <= target):
        #            break
        #        if one_list[index] > target:
        #            one_list[index] -= x
        #            counter += 1
        #        elif one_list[index] < target:
        #            one_list[index] += x
        #            counter += 1
        #        else:
        #            break
        #        #print(one_list[index])
##
        #return counter
    
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat_grid = [num for row in grid for num in row]
        flat_grid.sort()
        median = flat_grid[len(flat_grid) // 2]
        
        operations = 0
        for num in flat_grid:
            if abs(num - median) % x != 0:
                return -1
            operations += abs(num - median) // x
        
        return operations  
    
if __name__ == "__main__":
    solution = Solution()
    
    grid1 = [[2,4],[6,8]]
    x1 = 2
    print(solution.minOperations(grid1, x1))  # Output: 4
    
    grid2 = [[1,5],[2,3]]
    x2 = 1
    print(solution.minOperations(grid2, x2))  # Output: 5
    
    grid3 = [[1,2],[3,4]]
    x3 = 2
    print(solution.minOperations(grid3, x3))  # Output: -1

    grid4 = [[931,128],[639,712]]
    x4 = 73
    print(solution.minOperations(grid4, x4))  # Output: 12