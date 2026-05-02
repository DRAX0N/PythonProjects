"""
1878. Get Biggest Three Rhombus Sums in a Grid
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:


Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.

 

Example 1:


Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211
Example 2:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [20,9,8]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)
Example 3:

Input: grid = [[7,7,7]]
Output: [7]
Explanation: All three possible rhombus sums are the same, so return [7].
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 105
"""

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        def unique_sum(l,c,k,grid):
            if k == 0:
                return grid[l][c]
            
            sum = 0
            for n in range(k+1):
                sum += grid[l-k+n][c+n]
                sum += grid[l+n][c-k+n]

                sum += grid[l-k+n][c-n]
                sum += grid[l+n][c+k-n]

            sum -= grid[l+k][c] + grid[l-k][c] + grid[l][c+k] + grid[l][c-k]

            return sum
        
        def if_max(value,max_list):
            if value in max_list:
                return max_list
            elif value > max_list[0]:
                max_list.pop()
                max_list = [value, max_list[0], max_list[1]]
            elif value > max_list[1]:
                max_list.pop()
                max_list = [max_list[0], value, max_list[1]]

            elif value > max_list[2]:
                max_list.pop()
                max_list.append(value)
            return max_list

        max = [0]*3

        m, n = len(grid), len(grid[0]) 
        for l in range(m):
            for c in range(n):
                k = min(min(l, m-l-1), min(c, n-c-1))
                while k>=0:
                    value = unique_sum(l,c,k,grid)
                    max = if_max(value, max)
                    k-=1
                    
        while 0 in max:
            max.pop()

        return max



import heapq


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:

        m, n = len(grid), len(grid[0])
        diagonalPrefixSum = [[0] * (n + 2) for _ in range(m + 2)]
        antiDiagonalPrefixSum = [[0] * (n + 2) for _ in range(m + 2)]

        ans = []

        for r in range(m):
            for c in range(n):
                ur, uc = r + 1, c + 1
                diagonalPrefixSum[ur][uc] = (
                    grid[r][c] + diagonalPrefixSum[ur - 1][uc - 1]
                )
                antiDiagonalPrefixSum[ur][uc] = (
                    grid[r][c] + antiDiagonalPrefixSum[ur - 1][uc + 1]
                )

        for r in range(m):
            for c in range(n):

                # find largest rhombus with this at bottom
                largest_horizontal = min(c, n - 1 - c)
                largest_vertical = r // 2
                largest = min(largest_horizontal, largest_vertical)

                ur, uc = r + 1, c + 1

                for _ in range(3):

                    if largest < 0:
                        break
                    elif largest == 0:
                        rhombus = grid[r][c]
                    else:
                        rhombus = 0

                        rhombus += diagonalPrefixSum[ur][uc]
                        rhombus += antiDiagonalPrefixSum[ur][uc]
                        rhombus += diagonalPrefixSum[ur - largest][uc + largest]
                        rhombus += antiDiagonalPrefixSum[ur - largest][uc - largest]

                        rhombus -= diagonalPrefixSum[ur - largest - 1][uc - largest - 1]
                        rhombus -= antiDiagonalPrefixSum[ur - largest - 1][
                            uc + largest + 1
                        ]
                        rhombus -= diagonalPrefixSum[ur - 2 * largest - 1][uc - 1]
                        rhombus -= antiDiagonalPrefixSum[ur - 2 * largest - 1][uc + 1]

                        rhombus -= grid[r][c]
                        rhombus -= grid[r - largest][c - largest]
                        rhombus -= grid[r - 2 * largest][c]
                        rhombus -= grid[r - largest][c + largest]

                    if rhombus not in ans:
                        if len(ans) < 3:
                            heapq.heappush(ans, rhombus)
                        else:
                            heapq.heappushpop(ans, rhombus)

                    largest -= 1

        return sorted(ans, reverse=True)

if __name__ == "__main__":
    s = Solution()
    print(s.getBiggestThree([[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]])) # [228,216,211]
    print(s.getBiggestThree([[1,2,3],[4,5,6],[7,8,9]])) # [20,9,8]
    print(s.getBiggestThree([[7,7,7]])) # [7]
