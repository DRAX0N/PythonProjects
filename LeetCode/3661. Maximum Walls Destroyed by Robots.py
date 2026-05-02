"""
3661. Maximum Walls Destroyed by Robots
Hard
Topics
premium lock icon
Companies
Hint
There is an endless straight line populated with some robots and walls. You are given integer arrays robots, distance, and walls:
robots[i] is the position of the ith robot.
distance[i] is the maximum distance the ith robot's bullet can travel.
walls[j] is the position of the jth wall.
Every robot has one bullet that can either fire to the left or the right at most distance[i] meters.

A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it immediately stops at that robot and cannot continue.

Return the maximum number of unique walls that can be destroyed by the robots.

Notes:

A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.
Robots are not destroyed by bullets.
 

Example 1:

Input: robots = [4], distance = [3], walls = [1,10]

Output: 1

Explanation:

robots[0] = 4 fires left with distance[0] = 3, covering [1, 4] and destroys walls[0] = 1.
Thus, the answer is 1.
Example 2:

Input: robots = [10,2], distance = [5,1], walls = [5,2,7]

Output: 3

Explanation:

robots[0] = 10 fires left with distance[0] = 5, covering [5, 10] and destroys walls[0] = 5 and walls[2] = 7.
robots[1] = 2 fires left with distance[1] = 1, covering [1, 2] and destroys walls[1] = 2.
Thus, the answer is 3.
Example 3:
Input: robots = [1,2], distance = [100,1], walls = [10]

Output: 0

Explanation:

In this example, only robots[0] can reach the wall, but its shot to the right is blocked by robots[1]; thus the answer is 0.

 

Constraints:

1 <= robots.length == distance.length <= 105
1 <= walls.length <= 105
1 <= robots[i], walls[j] <= 109
1 <= distance[i] <= 105
All values in robots are unique
All values in walls are unique
"""

from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        walls.sort()
        #print(walls)
        robots_distance = sorted(zip(robots, distance), key=lambda x: x[0])
        robots_distance.sort()
        #print(robots_distance)
        res = 0
        wall_index = [0]*len(walls)
        for i in range(n):
            left_checker = robots_distance[i][0] - robots_distance[i][1] if robots_distance[i][0] - robots_distance[i][1] > 0 else 0
            right_checker = robots_distance[i][0] + robots_distance[i][1]

            # robot check
            # check NEAREST ROBOT
            for j in range(i-1, -1, -1):
                if left_checker <= robots_distance[j][0] <= robots_distance[i][0]:
                    left_checker = robots_distance[j][0]
            for j in range(i+1, n):
                if robots_distance[i][0] <= robots_distance[j][0] <= right_checker:
                    right_checker = robots_distance[j][0]

            # wall check
            left_index = [ 1 if left_checker <= w <= robots_distance[i][0] else 0 for w in walls]
            right_index = [ 1 if robots_distance[i][0] <= w <= right_checker else 0 for w in walls]

            #all_index = [ left_index[index]|right_index[index] for index in range(len(walls))]
            if sum([wall_index[index]|left_index[index] for index in range(len(walls))])>=sum([wall_index[index]|right_index[index] for index in range(len(walls))]):
                all_index = left_index
            else:
                all_index = right_index
                

            wall_index = [wall_index[index]|all_index[index] for index in range(len(walls))]
            #print(left_index)
            #print(right_index)
            #print(all_index)
            #print("=========================")
        res += sum(wall_index)
        return res



from bisect import bisect_left, bisect_right
from functools import cache

class Solution:
    def maxWalls(self, robots, distance, walls):
        n = len(robots)
        # Krok 1: sortuj roboty i ściany po pozycji
        arr = sorted(zip(robots, distance), key=lambda x: x[0])
        walls.sort()

        def count_walls(l, r):
            if l > r:
                return 0
            return bisect_right(walls, r) - bisect_left(walls, l)

        @cache
        def dfs(i, next_dir):
            # next_dir = kierunek w jakim strzela robot i+1 (0=lewo, 1=prawo)
            if i < 0:
                return 0

            pos, dist = arr[i]

            # --- Opcja 1: robot i strzela w LEWO ---
            left_l = pos - dist
            # lewa granica nie może wchodzić na poprzedniego robota
            if i > 0:
                left_l = max(left_l, arr[i-1][0] + 1)
            walls_left = count_walls(left_l, pos)
            # robot i strzela lewo -> dla robota i-1 next_dir=0
            result_left = dfs(i-1, 0) + walls_left

            # --- Opcja 2: robot i strzela w PRAWO ---
            right_r = pos + dist
            # prawa granica zależy od tego co robi robot i+1
            if i + 1 < n:
                if next_dir == 0:  # robot i+1 strzela lewo - bullet też leci lewo, więc nie blokuje
                    right_r = min(right_r, arr[i+1][0] - arr[i+1][1] - 1)
                else:              # robot i+1 strzela prawo - blokuje od swojej pozycji
                    right_r = min(right_r, arr[i+1][0] - 1)
            walls_right = count_walls(pos, right_r)
            # robot i strzela prawo -> dla robota i-1 next_dir=1
            result_right = dfs(i-1, 1) + walls_right

            return max(result_left, result_right)

        # Startujemy od ostatniego robota, zakładamy że "następny" (nieistniejący) strzela prawo
        return dfs(n - 1, 1)
    
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        # pair robots with their distances and sort by position
        rob = sorted(zip(robots, distance))
        p = [r[0] for r in rob]
        d = [r[1] for r in rob]

        # count walls that are exactly at a robot position
        robot_set = set(p)
        ans0 = 0
        walls_filtered = []
        for w in walls:
            if w in robot_set:
                ans0 += 1
            else:
                walls_filtered.append(w)
        walls_filtered.sort()
        m = len(walls_filtered)

        if m == 0:
            return ans0

        # ----- left region (walls before the first robot) -----
        left_count = 0
        j = 0
        while j < m and walls_filtered[j] < p[0]:
            if walls_filtered[j] >= p[0] - d[0]:
                left_count += 1
            j += 1

        # ----- gaps between consecutive robots -----
        # for each gap we store: only left robot can cover, only right robot can cover, both can cover
        left_only = [0] * (n - 1)
        right_only = [0] * (n - 1)
        both = [0] * (n - 1)

        for i in range(n - 1):
            start = p[i]
            end = p[i + 1]
            while j < m and walls_filtered[j] < end:
                if walls_filtered[j] > start:
                    distL = walls_filtered[j] - start
                    distR = end - walls_filtered[j]
                    if distL <= d[i] and distR <= d[i + 1]:
                        both[i] += 1
                    elif distL <= d[i]:
                        left_only[i] += 1
                    elif distR <= d[i + 1]:
                        right_only[i] += 1
                    # else: not coverable by any robot
                j += 1

        # ----- right region (walls after the last robot) -----
        right_count = 0
        while j < m and walls_filtered[j] <= p[-1] + d[-1]:
            right_count += 1
            j += 1

        # ----- DP over robots -----
        # dpL: best total if current robot fires left
        # dpR: best total if current robot fires right
        dpL = left_count   # robot 0 fires left
        dpR = 0            # robot 0 fires right

        for i in range(1, n):
            idx = i - 1
            A = left_only[idx] + both[idx]      # covered if left robot fires right
            B = right_only[idx] + both[idx]     # covered if right robot fires left
            C = left_only[idx] + right_only[idx] + both[idx]  # covered if both fire appropriately

            new_dpL = max(dpL + B, dpR + C)   # current robot fires left
            new_dpR = max(dpL, dpR + A)       # current robot fires right
            dpL, dpR = new_dpL, new_dpR

        result = ans0 + max(dpL, dpR + right_count)
        return result
     
if __name__ == "__main__": 
    s = Solution()
    print(s.maxWalls([4], [3], [1,10])) # 1
    print(s.maxWalls([10,2], [5,1], [5,2,7])) # 3
    print(s.maxWalls([1,2], [100,1], [10])) # 0
    robots = [17,59,32,11,72,18]
    distance = [5,7,6,5,2,10]
    walls = [17,25,33,29,54,53,18,35,39,37,20,14,34,13,16,58,22,51,56,27,10,15,12,23,45,43,21,2,42,7,32,40,8,9,1,5,55,30,38,4,3,31,36,41,57,28,11,49,26,19,50,52,6,47,46,44,24,48]
    print(s.maxWalls(robots, distance, walls)) # 37