"""
3548. Equal Sum Grid Partition II
Hard
Topics
premium lock icon
Companies
Hint
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of elements in both sections is equal, or can be made equal by discounting at most one single cell in total (from either section).
If a cell is discounted, the rest of the section must remain connected.
Return true if such a partition exists; otherwise, return false.

Note: A section is connected if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.

 

Example 1:

Input: grid = [[1,4],[2,3]]

Output: true

Explanation:



A horizontal cut after the first row gives sums 1 + 4 = 5 and 2 + 3 = 5, which are equal. Thus, the answer is true.
Example 2:

Input: grid = [[1,2],[3,4]]

Output: true

Explanation:



A vertical cut after the first column gives sums 1 + 3 = 4 and 2 + 4 = 6.
By discounting 2 from the right section (6 - 2 = 4), both sections have equal sums and remain connected. Thus, the answer is true.
Example 3:

Input: grid = [[1,2,4],[2,3,5]]

Output: false

Explanation:



A horizontal cut after the first row gives 1 + 2 + 4 = 7 and 2 + 3 + 5 = 10.
By discounting 3 from the bottom section (10 - 3 = 7), both sections have equal sums, but they do not remain connected as it splits the bottom section into two parts ([2] and [5]). Thus, the answer is false.
Example 4:

Input: grid = [[4,1,8],[3,2,6]]

Output: false

Explanation:

No valid cut exists, so the answer is false.

 

Constraints:

1 <= m == grid.length <= 105
1 <= n == grid[i].length <= 105
2 <= m * n <= 105
1 <= grid[i][j] <= 105
"""

from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        H, W = len(grid), len(grid[0])

        row_sums = list(map(sum, grid))
        col_sums = [ sum(grid[r][c] for r in range(H)) for c in range(W) ]
        total_sum = sum(row_sums)

        # Try cutting rows first
        # row_cut is the row index of the top row of the BOTTOM HALF
        row_cut = 0
        top_sum = 0
        bottom_sum = total_sum

        # max legal value for row_cut is H-1
        # But we will allow row_cut to be H in the loop to trigger the "reverse time by 1 step" handling
        for row_cut in range(1, H+1):

            top_sum += row_sums[row_cut-1]
            bottom_sum -= row_sums[row_cut-1]

            if top_sum == bottom_sum:
                print(f"At row_cut {row_cut}, top/bottom sum is {top_sum}/{bottom_sum}")
                return True
            elif top_sum > bottom_sum:

                # Let's look for something to discount
                top_discountable = set()
                if row_cut == 1:
                    # Only the top row is on the top, and removing cells in the middle
                    # will lead to disconnections
                    top_discountable = { grid[row_cut-1][0], grid[row_cut-1][W-1] }
                elif W == 1:
                    # The width is one, and removing any cells except the top and bottom
                    # from the top section will lead to disconnections
                    top_discountable = { grid[0][0], grid[row_cut-1][0] }
                else:
                    # No cell will cause disconnections
                    top_discountable = { grid[r][c] for r in range(row_cut) for c in range(W) }

                difference = top_sum - bottom_sum
                if difference in top_discountable:
                    print(f"At row_cut {row_cut}, top/bottom sum is {top_sum}/{bottom_sum}")
                    print(f"The difference is discountable: {top_discountable}")
                    return True

                # Last resort, let's check if we can rewind by one step
                # to make bottom_sum the bigger value, and then look for a discount in the

                # Rewinding by one step would make top_sum decrease by row_sum[row_cut-1]
                # and increase bottom_sum by the same amount, and their difference would be

                difference_alt = (bottom_sum + 2*row_sums[row_cut-1]) - top_sum
                
                # Let's look for something to discount in the bottom
                if row_cut == H:
                    # If row_cut is currently H, then "rewind by 1" means grid[H-1] is the top row
                    # of the bottom half
                    bottom_discountable = { grid[H-1][0], grid[H-1][W-1] }
                elif W == 1:
                    # The width is one, and removing any cells except the top and bottom
                    # from the top section will lead to disconnections
                    bottom_discountable = { grid[row_cut-1][0], grid[H-1][0] }
                else:
                    bottom_discountable = { grid[r][c] for r in range(row_cut-1, H) for c in range(W) }

                if difference_alt in bottom_discountable:
                    print(f"At row_cut {row_cut}, minus 1, top/bottom sum is {top_sum}/{bottom_sum}")
                    print(f"The adjusted difference {difference_alt} is discountable: {bottom_discountable}")
                    return True
                else:
                    # Should we keep checking? It depends
                    smallest_top = top_sum - max(top_discountable)
                    if smallest_top < bottom_sum:
                        # There's still a chance we can use a discount to find a solution
                        
                        continue
                    elif row_cut == 1:
                        # top_discountable might grow bigger on the next round, let's try again anyway
                        continue
                    else:
                        break

        col_cut = 0
        left_sum = 0
        right_sum = total_sum

        for col_cut in range(1, W+1):

            left_sum += col_sums[col_cut-1]
            right_sum -= col_sums[col_cut-1]

            if left_sum == right_sum:
                print(f"At col_cut {col_cut}, left/right sum is {left_sum}/{right_sum}")
                return True
            elif left_sum > right_sum:

                # Let's look for something to discount
                left_discountable = set()
                if col_cut == 1:
                    left_discountable = { grid[0][0], grid[H-1][0] }
                elif H == 1:
                    # The height is one, and removing any cells except the left and right
                    # from the left section will lead to disconnections
                    left_discountable = { grid[0][0], grid[0][col_cut-1] }
                else:
                    left_discountable = { grid[r][c] for c in range(col_cut) for r in range(H) }

                difference = left_sum - right_sum
                if difference in left_discountable:
                    print(f"At col_cut {col_cut}, left/right sum is {left_sum}/{right_sum}")
                    print(f"The difference {difference} is discountable on the left: {left_discountable}")
                    return True

                # Last resort, let's check if we can rewind by one step
                # to make right_sum the bigger value, and then look for a discount in the

                # Rewinding by one step would make left_sum decrease by col_sum[col_cut-1]
                # and increase right_sum by the same amount, and their difference would be

                difference_alt = (right_sum + 2*col_sums[col_cut-1]) - left_sum
                
                # Let's look for something to discount in the bottom
                if col_cut == W:
                    right_discountable = { grid[0][W-1], grid[H-1][W-1] }
                elif H == 1:
                    # The height is one, and removing any cells except the left and right
                    # from the right section will lead to disconnections
                    right_discountable = { grid[0][col_cut-1], grid[0][W-1] }
                else:
                    right_discountable = { grid[r][c] for c in range(col_cut-1, W) for r in range(H) }

                if difference_alt in right_discountable:
                    print(f"At col_cut {col_cut}, minus 1, left/right sum is {left_sum}/{right_sum}")
                    print(f"The adjust difference {difference_alt} is discountable on the right: {right_discountable}")
                    return True
                else:
                    # Should we keep checking? It depends
                    smallest_left = left_sum - max(left_discountable)
                    if smallest_left < right_sum:
                        # There's still a chance we can use a discount to find a solution
                        
                        continue
                    elif col_cut == 1:
                        # left_discountable might grow bigger on the next round, let's try again anyway
                        continue
                    else:
                        break

        return False
    
class Solution:
  def canPartitionGrid(self, grid: list[list[int]]) -> bool:
    summ = sum(map(sum, grid))

    def canPartition(grid: list[list[int]]) -> bool:
      topSum = 0
      seen = set()
      for i, row in enumerate(grid):
        topSum += sum(row)
        botSum = summ - topSum
        seen |= set(row)
        if topSum - botSum in (0, grid[0][0],  grid[0][-1], row[0]):
          return True
        if len(grid[0]) > 1 and i > 0 and topSum - botSum in seen:
          return True
      return False

    return (canPartition(grid) or
            canPartition(grid[::-1]) or
            canPartition(list(zip(*grid))[::-1]) or
            canPartition(list(zip(*grid))))

if __name__ == "__main__":
    s = Solution()
    print(s.canPartitionGrid([[1,4],[2,3]])) # true
    print(s.canPartitionGrid([[1,2],[3,4]])) # true
    print(s.canPartitionGrid([[1,2,4],[2,3,5]])) # false
    print(s.canPartitionGrid([[4,1,8],[3,2,6]])) # false
    print(s.canPartitionGrid([[29700],[29700]])) # True
    print(s.canPartitionGrid([[5,5,6,2,2,2]])) # True
