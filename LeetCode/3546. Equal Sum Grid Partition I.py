"""
3546. Equal Sum Grid Partition I
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of the elements in both sections is equal.
Return true if such a partition exists; otherwise return false.

 

Example 1:

Input: grid = [[1,4],[2,3]]

Output: true

Explanation:



A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.

Example 2:

Input: grid = [[1,3],[2,4]]

Output: false

Explanation:

No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.

 

Constraints:

1 <= m == grid.length <= 105
1 <= n == grid[i].length <= 105
2 <= m * n <= 105
1 <= grid[i][j] <= 105
"""

from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total_sum = 0
        for i in range(m):
            for j in range(n):
                total_sum += grid[i][j]

        if total_sum%2 != 0:
            return False
        
        half = total_sum//2

        #horizontal
        for i in range(m):
            for j in range(n):
                number = grid[i][j]
                half -= number
                if half == 0 and j == (n-1):
                    return True
                elif half == 0 and m == 1:
                    second_half = 0
                    for index in range(j+1, n):
                        second_half += grid[0][index]
                    if second_half == total_sum//2:
                        return True
                    else:
                        return False
                elif half < 0:
                    break
            if half < 0:
                break

        #vertical
        half = total_sum//2   
        for j in range(n): 
            for i in range(m):
                number = grid[i][j]
                half -= number
                if half == 0 and i == (m-1):
                    return True
                elif half == 0 and n == 1:
                    second_half = 0
                    for index in range(i+1, m):
                        second_half += grid[index][0]
                    if second_half == total_sum//2:
                        return True
                    else:
                        return False
                elif half < 0:
                    break
            if half < 0:
                break

        return False
    
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # strategy:
        # 1. do a prefix sum of rows
        # 2. do a prefix sum of columns
        # 3. do one pass on rows and check if we can meet the conditions
        # 4. do one pass on columns and check if we can meet the conditions
        # 5. whenever we meet the conditions, return True
        # 6. otherwise, return False

        m = len(grid)
        n = len(grid[0])
        
        psr = []
        for i in range(m):
            psr.append((psr[-1] if i > 0 else 0) + sum(grid[i]))
        
        psc = []
        for i, column in enumerate(zip(*grid)):
            psc.append((psc[-1] if i > 0 else 0) + sum(column))
        
        for i in range(m - 1):
            a = psr[i]
            b = psr[-1] - (psr[i] if i >= 0 else 0)

            if a == b: return True
        
        for i in range(n - 1):
            a = psc[i]
            b = psc[-1] - (psc[i] if i >= 0 else 0)

            if a == b: return True
        
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.canPartitionGrid([[1,4],[2,3]])) # True
    print(s.canPartitionGrid([[1,3],[2,4]])) # False
    print(s.canPartitionGrid([[14742,71685,59237,27190]])) # True
    print(s.canPartitionGrid([[9753,4621,3652],[3003,4050,433]])) # True
