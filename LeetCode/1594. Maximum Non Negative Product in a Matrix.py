"""
1594. Maximum Non Negative Product in a Matrix
Medium
Topics
premium lock icon
Companies
Hint
You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.

Notice that the modulo is performed after getting the maximum product.

 

Example 1:


Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
Output: -1
Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
Example 2:


Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).
Example 3:


Input: grid = [[1,3],[0,-4]]
Output: 0
Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
-4 <= grid[i][j] <= 4
"""

from ast import List

class Solution:
        
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # Stała modulo 
        MODULO = 10**9 + 7
        # Rozmiary macierzy: m wierszy, n kolumn
        m, n = len(grid), len(grid[0])

        # max_product[i][j] przechowuje największy (aktualnie możliwy) iloczyn ścieżki
        # od (0,0) do (i,j)
        max_product = [[0] * n for _ in range(m)]
        # min_product[i][j] przechowuje najmniejszy (możliwy, czyli najbardziej ujemny)
        # iloczyn ścieżki od (0,0) do (i,j), bo ujemna * ujemna może dać pozytywny
        min_product = [[0] * n for _ in range(m)]

        # Inicjalizacja punktu startowego
        max_product[0][0] = min_product[0][0] = grid[0][0]

        # Wypełnij pierwszą kolumnę (możemy się poruszać tylko w dół)
        for i in range(1, m):
            max_product[i][0] = min_product[i][0] = max_product[i-1][0] * grid[i][0]

        # Wypełnij pierwszy wiersz (możemy się poruszać tylko w prawo)
        for j in range(1, n):
            max_product[0][j] = min_product[0][j] = max_product[0][j-1] * grid[0][j]

        # Dynamiczne programowanie dla pozostałych komórek
        for i in range(1, m):
            for j in range(1, n):
                # aktualna wartość na siatce
                val = grid[i][j]

                if val >= 0:
                    # Dodatnia wartość mnożona przez największy daje największy,
                    # a przez najmniejszy daje najmniejszy
                    max_product[i][j] = max(max_product[i-1][j], max_product[i][j-1]) * val
                    min_product[i][j] = min(min_product[i-1][j], min_product[i][j-1]) * val
                else:
                    # Ujemna wartość odwraca znaki: największy może powstać z najmniejszego
                    # i odwrotnie
                    max_product[i][j] = min(min_product[i-1][j], min_product[i][j-1]) * val
                    min_product[i][j] = max(max_product[i-1][j], max_product[i][j-1]) * val

        # Wynik z prawego dolnego rogu
        result = max_product[m-1][n-1]

        # Jeśli wynik nieujemny, zwróć go modulo, w przeciwnym razie -1
        return result % MODULO if result >= 0 else -1

if __name__ == '__main__':
    new = Solution()
    print(new.maxProductPath([[1,-2,1],[1,-2,1],[3,-4,1]]))#8
    print(new.maxProductPath([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]))#-1
    print(new.maxProductPath([[1,3],[0,-4]]))#0