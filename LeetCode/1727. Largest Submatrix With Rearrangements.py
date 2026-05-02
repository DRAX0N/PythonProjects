"""
1727. Largest Submatrix With Rearrangements
Medium
Topics
premium lock icon
Companies
Hint
You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

 

Example 1:


Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.
Example 2:


Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.
Example 3:

Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m * n <= 105
matrix[i][j] is either 0 or 1.
"""

from ast import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        #largest sunstring of 1 in whole matrix
        l_len = len(matrix[0])
        c_len = len(matrix)
        
        for i in range(1, c_len):
            for j in range(l_len):
                if matrix[i][j] == 1:
                    matrix[i][j] = matrix[i-1][j] + 1
        res = 0
        for i in range(c_len):
            matrix[i].sort(reverse=True)
            for j in range(l_len):
                res = max(res, matrix[i][j] * (j + 1))
        return res

        

        


if __name__ == "__main__":
    s = Solution()
    print(s.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]])) # 4
    print(s.largestSubmatrix([[1,0,1,0,1]])) # 3
    print(s.largestSubmatrix([[1,1,0],[1,0,1]])) # 2