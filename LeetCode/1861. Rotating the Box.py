'''
1861. Rotating the Box
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

 

Example 1:



Input: boxGrid = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
Example 2:



Input: boxGrid = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
Example 3:



Input: boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
 

Constraints:

m == boxGrid.length
n == boxGrid[i].length
1 <= m, n <= 500
boxGrid[i][j] is either '#', '*', or '.'.
'''

from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # * - block
        # # - falling rock
        # . - empty space
        n = len(boxGrid)
        m = len(boxGrid[0])
        
        for i in range(n):
            for j in range(m-2,-1,-1):
                while j != m - 1 or (j == m-2 and boxGrid[i][j+1] != '.'):
                    if boxGrid[i][j+1] == '.' and boxGrid[i][j] == '#':
                        boxGrid[i][j+1] = '#'
                        boxGrid[i][j] = '.'
                    j += 1
     
        res = [] 
        for j in range(m):
            temp = []
            for i in range(n-1,-1,-1):
                temp.append(boxGrid[i][j])
            res.append(temp)
        return res
    
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n = len(boxGrid)
        m = len(boxGrid[0])

        for i in range(n):
            empty = m - 1
            for j in range(m - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    empty = j - 1
                elif boxGrid[i][j] == '#':
                    if j != empty:
                        boxGrid[i][empty] = '#'
                        boxGrid[i][j] = '.'
                    empty -= 1

        res = []
        for j in range(m):
            temp = []
            for i in range(n - 1, -1, -1):
                temp.append(boxGrid[i][j])
            res.append(temp)

        return res
    
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        r, c=len(box), len(box[0])
        rotate=[['.']*r for _ in range(c)]
        for i, row in enumerate(box):
            bottom=c-1
            for j in range(c-1, -1, -1):
                if row[j]=='#':
                    rotate[bottom][r-1-i]='#'
                    bottom-=1
                elif row[j]=='*':
                    rotate[j][r-1-i]='*'
                    bottom=j-1
        return rotate
        
if __name__ == "__main__":
    s = Solution()
    print(s.rotateTheBox([["#",".","#"]]))  # Output: [["."], ["#"], ["#"]]
    print(s.rotateTheBox([["#",".","*","."],
                          ["#","#","*","."]]))  # Output: [["#","."], ["#","#"], ["*","*"], [".","."]]
    print(s.rotateTheBox([["#","#","*",".","*","."],
                          ["#","#","#","*",".","."],
                          ["#","#","#",".","#","."]]))  # Output: [[".","#","#"], [".","#","#"], ["#","#","*"], ["#","*","."], ["#",".","*"], ["#",".","."]]

