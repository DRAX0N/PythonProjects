"""
2267. Check if There Is a Valid Parentheses String Path
Hard
Topics
premium lock icon
Companies
Hint
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:

The path starts from the upper left cell (0, 0).
The path ends at the bottom-right cell (m - 1, n - 1).
The path only ever moves down or right.
The resulting parentheses string formed by the path is valid.
Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.

 

Example 1:


Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
Output: true
Explanation: The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.
Example 2:


Input: grid = [[")",")"],["(","("]]
Output: false
Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is either '(' or ')'.
"""
from functools import lru_cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        path_length = m + n - 1

        # Poprawny ciąg nawiasów zawsze ma parzystą długość.
        if path_length % 2 == 1:
            return False

        # Poprawna ścieżka nie może zaczynać się od ')' ani kończyć na '('.
        if grid[0][0] == ")" or grid[m - 1][n - 1] == "(":
            return False

        @lru_cache(maxsize=None)
        def dfs(row: int, col: int, balance: int) -> bool:
            # Dodaj nawias z aktualnego pola.
            balance += 1 if grid[row][col] == "(" else -1

            # Prefiks poprawnego ciągu nie może mieć więcej ')' niż '('.
            if balance < 0:
                return False

            # Tyle pól (włącznie z bieżącym) pozostało do końca.
            remaining_cells = (m - 1 - row) + (n - 1 - col)

            # Nawet gdy wszystkie następne znaki będą ')', nie zamkniemy balance.
            if balance > remaining_cells:
                return False

            if row == m - 1 and col == n - 1:
                return balance == 0

            return (
                (row + 1 < m and dfs(row + 1, col, balance))
                or
                (col + 1 < n and dfs(row, col + 1, balance))
            )

        return dfs(0, 0, 0)
    
from functools import cache
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Quick boundary checks
        if (m + n - 1) % 2 == 1 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        @cache
        def dfs(i: int, j: int, k: int) -> bool:
            # Update balance based on current cell
            k += 1 if grid[i][j] == '(' else -1
            
            # Prune invalid paths
            if k < 0 or k > m - i + n - j - 1:
                return False
                
            # Base case: reached bottom-right cell
            if i == m - 1 and j == n - 1:
                return k == 0
                
            # Move down or right
            res = False
            if i + 1 < m:
                res = res or dfs(i + 1, j, k)
            if not res and j + 1 < n:
                res = res or dfs(i, j + 1, k)
                
            return res

        return dfs(0, 0, 0)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.hasValidPath([["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]))  # Expected: True
    print(solution.hasValidPath([[")",")"],["(","("]]))  # Expected: False