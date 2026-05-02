"""
3464. Maximize the Distance Between Points on a Square
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer side, representing the edge length of a square with corners at (0, 0), (0, side), (side, 0), and (side, side) on a Cartesian plane.

You are also given a positive integer k and a 2D integer array points, where points[i] = [xi, yi] represents the coordinate of a point lying on the boundary of the square.

You need to select k elements among points such that the minimum Manhattan distance between any two points is maximized.

Return the maximum possible minimum Manhattan distance between the selected k points.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.

 

Example 1:

Input: side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4

Output: 2

Explanation:



Select all four points.

Example 2:

Input: side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4

Output: 1

Explanation:



Select the points (0, 0), (2, 0), (2, 2), and (2, 1).

Example 3:

Input: side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5

Output: 1

Explanation:



Select the points (0, 0), (0, 1), (0, 2), (1, 2), and (2, 2).

 

Constraints:

1 <= side <= 109
4 <= points.length <= min(4 * side, 15 * 103)
points[i] == [xi, yi]
The input is generated such that:
points[i] lies on the boundary of the square.
All points[i] are unique.
4 <= k <= min(25, points.length)
"""

from collections import deque
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        #output of function should be the same as comment in line where function is called
        def can_select(distance: int) -> bool:
            selected = []
            for x, y in points:
                if all(abs(x - sx) + abs(y - sy) >= distance for sx, sy in selected):
                    selected.append((x, y))
                    if len(selected) == k:
                        return True
            return False

        left, right = 0, 2 * side
        while left < right:
            mid = (left + right + 1) // 2
            if can_select(mid):
                left = mid
            else:
                right = mid - 1
        return left
    
class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        # Mapowanie na obwód 1D
        def to_perim(x, y):
            if x == 0:      return y
            if y == side:   return side + x
            if x == side:   return 3 * side - y
            return 4 * side - x

        coords = sorted(to_perim(x, y) for x, y in points)
        n = len(coords)
        P = 4 * side

        def can_select(d):
            for i in range(n):
                cur, count = coords[i], 1
                limit = coords[i] + P - d  # nie "owijaj" więcej niż jeden raz
                for j in range(i + 1, i + n):
                    nxt = coords[j % n] + (P if j >= n else 0)
                    if nxt > limit:
                        break
                    if nxt - cur >= d:
                        cur, count = nxt, count + 1
                        if count == k:
                            return True
            return False

        lo, hi = 0, side
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_select(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
    

import bisect
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Mapowanie punktów na współrzędne 1D wzdłuż obwodu
        coords = []
        for x, y in points:
            if x == 0:
                coords.append(y)
            elif y == side:
                coords.append(side + x)
            elif x == side:
                coords.append(3 * side - y)
            else:  # y == 0
                coords.append(4 * side - x)
        coords.sort()
        n = len(coords)
        perimeter = 4 * side

        def can_select(d: int) -> bool:
            if d == 0:
                return True
            # Próbuj każdy punkt jako punkt startowy
            for i in range(n):
                current = coords[i]
                last_allowed = current + perimeter - d  # żeby obwód się "zamknął"
                count = 1
                for _ in range(k - 1):
                    # Szukaj binarnie następnego punktu >= current + d
                    # Uwzględniamy obwód przez extended array
                    j = bisect.bisect_left(coords, current + d)
                    if j < n and coords[j] <= last_allowed:
                        current = coords[j]
                        count += 1
                    else:
                        break
                if count == k:
                    return True
            return False

        left, right = 0, side  # max odległość Manhattan na kwadracie to `side`
        while left < right:
            mid = (left + right + 1) // 2
            if can_select(mid):
                left = mid
            else:
                right = mid - 1
        return left


class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        a = []
        for x, y in points:
            if x == 0:
                a.append(y)
            elif y == side:
                a.append(side + x)
            elif x == side:
                a.append(side * 3 - y)
            else:
                a.append(side * 4 - x)
        a.sort()

        def check(low: int) -> bool:
            idx = [0] * k
            cur = a[0]
            for j in range(1, k):
                i = bisect_left(a, cur + low)
                if i == len(a):
                    return False
                idx[j] = i
                cur = a[i]
            if cur - a[0] <= side * 4 - low:
                return True

            for idx[0] in range(1, idx[1]):
                for j in range(1, k):
                    while a[idx[j]] < a[idx[j - 1]] + low:
                        idx[j] += 1
                        if idx[j] == len(a):
                            return False
                if a[idx[-1]] - a[idx[0]] <= side * 4 - low:
                    return True
            return False

        left, right = 1, side + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left
    

if __name__ == "__main__":
    s = Solution()
    print(s.maxDistance(2, [[0,2],[2,0],[2,2],[0,0]], 4)) # 2
    print(s.maxDistance(2, [[0,0],[1,2],[2,0],[2,2],[2,1]], 4)) # 1
    print(s.maxDistance(2, [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], 5)) # 1
    print(s.maxDistance(4, [[4,4],[3,4],[2,0],[4,3],[4,0]], 4)) # 2