"""
3070. Count Submatrices with Top-Left Element and Sum Less Than k
Medium
Topics
premium lock icon
Companies
You are given a 0-indexed integer matrix grid and an integer k.

Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.

 

Example 1:


Input: grid = [[7,6,3],[6,6,1]], k = 18
Output: 4
Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.
Example 2:


Input: grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
Output: 6
Explanation: There are only 6 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 20.
 

Constraints:

m == grid.length 
n == grid[i].length
1 <= n, m <= 1000 
0 <= grid[i][j] <= 1000
1 <= k <= 109
"""

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] > k:
            return 0
        m, n = len(grid), len(grid[0])
        counter = 0
        # first line
        #sum = 0
        #for i in range(n):
        #    sum += grid[0][i]
        #    if sum <= k:
        #        counter += 1
        #    else:
        #        break
        #base = counter
#
        #for j in range(base):
        #    sum = 0
        #    for i in range(1,m):
        #        #petla na kwadrat
        #        sum += grid[i][j]
        #        if sum < k:
        #            counter += 1
        #        else:
        #            break

        #for i in range(n):
        #    
        #    print("?????????????????")
        #    print("i = " + str(i))
        #    print("?????????????????")
        #    for j in range(m):
        #        sum = 0
        #        #if i>0 and j>0:
        #        print("==================")
        #        
        #        print("j = " + str(j))
        #        for l in range(i+1):
        #            for c in range(j+1):
        #                #print(l)
        #                sum += grid[c][l]
        #        #else:
        #        #    sum += grid[i][j]
        #        if sum > k:
        #            print("sum = " + str(sum))
        #            break
        #        else:
        #            counter += 1
        #            print("sum = " + str(sum))
        #            print("counter = " + str(counter))
        #            print("------------------------")

        for i in range(n):
            for j in range(m):
                suma = 0
                for l in range(i+1):
                    for c in range(j+1):
                        suma += grid[c][l]
                        if suma > k:
                            break
                    if suma > k:
                        break
                if suma > k:
                    break
                else:
                    counter += 1

        return counter

from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        count = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (
                    grid[i - 1][j - 1]
                    + prefix[i - 1][j]
                    + prefix[i][j - 1]
                    - prefix[i - 1][j - 1]
                )

                if prefix[i][j] <= k:
                    count += 1

        return count

from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                top = grid[i - 1][j] if i > 0 else 0
                left = grid[i][j - 1] if j > 0 else 0
                diag = grid[i - 1][j - 1] if i > 0 and j > 0 else 0

                grid[i][j] = grid[i][j] + top + left - diag

                if grid[i][j] <= k:
                    ans += 1

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.countSubmatrices([[7,6,3],[6,6,1]], 18)) # 4
    print(s.countSubmatrices([[7,2,9],[1,5,0],[2,6,6]], 20)) # 6
