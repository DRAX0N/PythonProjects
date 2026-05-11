"""

Code
Testcase
Testcase
Test Result
1914. Cyclically Rotating a Grid
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:



A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:


Return the matrix after applying k cyclic rotations to it.

 

Example 1:


Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]
Explanation: The figures above represent the grid at every state.
Example 2:


Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
Explanation: The figures above represent the grid at every state.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 50
Both m and n are even integers.
1 <= grid[i][j] <= 5000
1 <= k <= 109
"""

from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            elements = []
            # Top row
            for j in range(layer, n - layer):
                elements.append(grid[layer][j])
            # Right column
            for i in range(layer + 1, m - layer):
                elements.append(grid[i][n - layer - 1])
            # Bottom row
            for j in range(n - layer - 2, layer - 1, -1):
                elements.append(grid[m - layer - 1][j])
            # Left column
            for i in range(m - layer - 2, layer, -1):
                elements.append(grid[i][layer])

            # Rotate the elements
            k_mod = k % len(elements)
            rotated = elements[k_mod:] + elements[:k_mod]

            idx = 0
            # Place back the rotated elements
            for j in range(layer, n - layer):
                grid[layer][j] = rotated[idx]
                idx += 1
            for i in range(layer + 1, m - layer):
                grid[i][n - layer - 1] = rotated[idx]
                idx += 1
            for j in range(n - layer - 2, layer - 1, -1):
                grid[m - layer - 1][j] = rotated[idx]
                idx += 1
            for i in range(m - layer - 2, layer, -1):
                grid[i][layer] = rotated[idx]
                idx += 1

        return grid
    
if __name__ == "__main__":
    s = Solution()
    print(s.rotateGrid([[40,10],[30,20]], 1))  # [[10,20],[40,30]]
    print(s.rotateGrid([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2))  # [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]