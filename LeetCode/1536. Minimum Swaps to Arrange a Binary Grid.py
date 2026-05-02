"""
1536. Minimum Swaps to Arrange a Binary Grid
Medium
Topics
premium lock icon
Companies
Hint
Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

 

Example 1:


Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
Example 2:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.
Example 3:


Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
grid[i][j] is either 0 or 1
"""

#class Solution:
#    def minSwaps(self, grid: List[List[int]]) -> int:
#        #def is_valid(grid):
#        #    isvalid = False
#        #    for row_number in range(len(grid)-1):
#        #        if grid[row_number][row_number+1:] == [0]*(len(grid)-1-row_number):
#        #            isvalid = True
#        #        else:    
#        #            return False
#        #    return isvalid
#        def is_valid_right(row):
#            isvalid = False
#            for number in range(len(row)-1):
#                if row[number] <= number:
#                    isvalid = True
#                else:    
#                    return False
#            return isvalid
#        
#        counter = 0 
#        max_counter = 0 
#
#        #if is_valid(grid):
#        #    return counter
#        
#        for i in range(len(grid)):
#            max_counter += i
#
#        most_right = [-1]*len(grid)
#        for index, row in enumerate(grid):
#            r = len(grid)-1
#            while r>=0:
#                if row[r] == 1:
#                    most_right[index] = r
#                    break
#                else:
#                    r -= 1
#        print("max right " + str(most_right))
#        print("max_counter: " + str(max_counter))
#        print("is valid max right: " + str(is_valid_right(most_right)))
#        while (not is_valid_right(most_right)) and counter <= max_counter:
#            print("===========================================")
#            temp = most_right
#            #for index, maxR in enumerate(temp[::-1]):
#            for index in range(len(temp)-1, -1, -1):
#                maxR = temp[index]
#                print("index: " + str(index) + ", maxR: " + str(maxR))
#                if index != len(temp)-1 and maxR <= index and (index == 0 or maxR <= temp[index+1]):
#                    print("op1")
#                    continue
#                elif maxR <= index and maxR <= temp[index+1]: 
#                    print("op2")
#                    most_right[index] = temp[index-1]
#                    most_right[index-1] = maxR                   
#                    counter += 1
#                    break
#                elif maxR > index and maxR != temp[index+1]:
#                    print("op3")
#                    most_right[index] = temp[index+1]
#                    most_right[index+1] = maxR
#                    counter += 1
#                    break
#
#            #print(temp)
#            print(most_right)
#            #print("counter "+ str(counter))
#            #print(is_valid_right(most_right))
#            #print((not is_valid_right(most_right)) and counter <= max_counter)
#        if counter >  max_counter:
#            return -1
#        else:
#            return counter
        
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n_len = len(grid)
        most_rights = []
        for row in grid:
            for j in range(n_len - 1, -1, -1):
                if row[j] == 1:
                    most_rights.append(j)
                    break
            else:
                most_rights.append(0)
        
        counter = 0
        max_counter = 0
        max_valid_righs = [x for x in range(n_len)]
        max_counter = sum(max_valid_righs)
        print("max_counter: " + str(max_counter))


        for i in range(n_len):  # 2. Dla każdego docelowego wiersza i
            # Potrzebujemy pos[row] <= i
            
            # Znajdź najbliższy odpowiedni wiersz od i w dół
            target_row = -1
            for j in range(i, n_len):
                if most_rights[j] <= i:
                    target_row = j
                    break
            
            if target_row == -1:  # Brak odpowiedniego wiersza
                return -1
            
            # 3. Przesuń target_row do pozycji i (bubble up)
            counter += target_row - i
            for k in range(target_row, i, -1):
                most_rights[k], most_rights[k - 1] = most_rights[k - 1], most_rights[k]



        if counter >  max_counter:
            return -1
        else:
            return counter
    
if __name__ == '__main__':
    #grid = [[0,0,1],[1,1,0],[1,0,0]]    # output 3
    #grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]    # output -1

    grid = [[1,0,0],[1,1,0],[1,1,1]]    # output 0
    grid = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]    # 2
    grid = [[1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,1]] #4
    new = Solution()
    print(new.minSwaps(grid)) 