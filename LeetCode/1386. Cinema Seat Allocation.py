"""
1386. Cinema Seat Allocation
Medium
Topics
premium lock icon
Companies
Hint


A cinema has n rows of seats, numbered from 1 to n. Each row has 10 seats, numbered from 1 to 10.

You are given a 2D integer array reservedSeats, where reservedSeats[i] = [rowi, seati] means that seat seati in row rowi is already reserved.

A four-person group must be assigned to four seats in the same row. The group can be seated in one of the following seat blocks:

seats 2, 3, 4, 5
seats 4, 5, 6, 7
seats 6, 7, 8, 9
A block can be used only if none of its seats are reserved. Each seat can be assigned to at most one group.

Return an integer denoting the maximum number of four-person groups that can be assigned.

 

Example 1:



Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.
Example 2:

Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2
Example 3:

Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4
 

Constraints:

1 <= n <= 109
1 <= reservedSeats.length <= min(10 * n, 104)
reservedSeats[i] == [rowi, seati]
1 <= rowi <= n
1 <= seati <= 10
All reservedSeats[i] are distinct.
"""
from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(set)

        for row, seat in reservedSeats:
            if seat in [2, 3, 4, 5]:
                seats[row].add(0)
            
            if seat in [4, 5, 6, 7]:
                seats[row].add(1)
            
            if seat in [6, 7, 8, 9]:
                seats[row].add(2)
        
        total = 2 * n

        for i in seats:
            if len(seats[i]) == 3:
                total-= 2
            else:
                total-= 1
        
        return total
    
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        c = defaultdict(int)
        for r, s in reservedSeats:
            if 1 < s < 10:
                c[r] |= 1 << (s-2)
        return (n-len(c))*2 + sum(0 in (r&15, r&60, r&240) for r in c.values())
    
if __name__ == "__main__":
    sol = Solution()
    n = 3
    reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
    print(sol.maxNumberOfFamilies(n, reservedSeats))  # Output: 4

    n = 2
    reservedSeats = [[2,1],[1,8],[2,6]]
    print(sol.maxNumberOfFamilies(n, reservedSeats))  # Output: 2

    n = 4
    reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
    print(sol.maxNumberOfFamilies(n, reservedSeats))  # Output: 4