"""
2463. Minimum Total Distance Traveled
Hard
Topics
premium lock icon
Companies
Hint
There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.

The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.

All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.

At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.

Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.

Note that

All robots move at the same speed.
If two robots move in the same direction, they will never collide.
If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
If the robot moved from a position x to a position y, the distance it moved is |y - x|.
 

Example 1:


Input: robot = [0,4,6], factory = [[2,2],[6,2]]
Output: 4
Explanation: As shown in the figure:
- The first robot at position 0 moves in the positive direction. It will be repaired at the first factory.
- The second robot at position 4 moves in the negative direction. It will be repaired at the first factory.
- The third robot at position 6 will be repaired at the second factory. It does not need to move.
The limit of the first factory is 2, and it fixed 2 robots.
The limit of the second factory is 2, and it fixed 1 robot.
The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that we cannot achieve a better total distance than 4.
Example 2:


Input: robot = [1,-1], factory = [[-2,1],[2,1]]
Output: 2
Explanation: As shown in the figure:
- The first robot at position 1 moves in the positive direction. It will be repaired at the second factory.
- The second robot at position -1 moves in the negative direction. It will be repaired at the first factory.
The limit of the first factory is 1, and it fixed 1 robot.
The limit of the second factory is 1, and it fixed 1 robot.
The total distance is |2 - 1| + |(-2) - (-1)| = 2. It can be shown that we cannot achieve a better total distance than 2.
 

Constraints:

1 <= robot.length, factory.length <= 100
factory[j].length == 2
-109 <= robot[i], positionj <= 109
0 <= limitj <= robot.length
The input will be generated such that it is always possible to repair every robot.
"""
from typing import List
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        n = len(robot)
        m = len(factory)
        dp = [[float("inf")] * (m+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(n+1):
            for j in range(m):
                dp[i][j+1] = min(dp[i][j+1], dp[i][j])
                cur = 0
                for k in range(1, factory[j][1]+1):
                    if i+k > n:
                        break
                    cur += abs(robot[i+k-1] - factory[j][0])
                    dp[i+k][j+1] = min(dp[i+k][j+1], dp[i][j] + cur)
        return dp[n][m]
    
from dataclasses import dataclass
from typing import List


@dataclass
class Factory:
    pos: int
    capacity: int
    used: int = 0
    first_bot_idx: int = -1  # Index of the first robot currently in this factory
    shift_penalty: int = 0 # Cost to move the first robot to the previous factory


class Solution:
    def minimumTotalDistance(self, robots: List[int], factory: List[List[int]]) -> int:
        robots.sort()
        
        # Add boundary sentinels to avoid index-out-of-bounds
        factories_data = [[-int(1e15), 1]] + sorted(f for f in factory if f[1] > 0) + [[int(1e15), 1]]
        
        factories = [
            Factory(pos=f[0], capacity=f[1]) for f in factories_data
        ]

        def update_shift_penalty(f_idx: int):
            """Calculates penalty to move the 'first' robot of factory[f_idx] to factory[f_idx-1]."""
            curr_f = factories[f_idx]
            prev_f = factories[f_idx - 1]
            bot_pos = robots[curr_f.first_bot_idx]
            
            # Penalty = (Distance to previous factory) - (Distance to current factory)
            curr_f.shift_penalty = abs(bot_pos - prev_f.pos) - abs(bot_pos - curr_f.pos)

        def assign_and_shift(bot_idx: int, f_idx: int):
            """Recursively shifts robots left if the chosen factory is full."""
            target_f = factories[f_idx]
            
            while target_f.used == target_f.capacity:
                # Kick the leftmost robot out of this factory
                displaced_bot_idx = target_f.first_bot_idx
                target_f.first_bot_idx += 1
                update_shift_penalty(f_idx)
                
                # The displaced robot now needs to be handled by the previous factory
                bot_idx = displaced_bot_idx
                f_idx -= 1
                target_f = factories[f_idx]
                
            if target_f.used == 0:
                target_f.first_bot_idx = bot_idx
                
            target_f.used += 1
            if target_f.used > 0:
                update_shift_penalty(f_idx)

        total_ans = 0
        factory_ptr = 1 # Start at the first real factory (skipping -inf)

        for bot_idx, bot_pos in enumerate(robots):
            # 1. Find the current factory
            if factories[factory_ptr].pos < bot_pos:
                while factories[factory_ptr + 1].pos < bot_pos:
                    factory_ptr += 1
            
            # 2. Calculate cost to go RIGHT
            right_cost = factories[factory_ptr + 1].pos - bot_pos
            
            # 3. Calculate cost to go LEFT (including all shift penalties)
            left_cost = abs(factories[factory_ptr].pos - bot_pos)
            
            # If the left factory is full, we must add the penalties of shifting its robots
            temp_idx = factory_ptr
            while factories[temp_idx].used == factories[temp_idx].capacity:
                left_cost += factories[temp_idx].shift_penalty
                temp_idx -= 1
                
            # 4. Make the greedy decision
            if left_cost <= right_cost:
                total_ans += left_cost
                assign_and_shift(bot_idx, factory_ptr)
            else:
                factory_ptr += 1
                total_ans += right_cost
                assign_and_shift(bot_idx, factory_ptr)

        return total_ans       
    
if __name__ == "__main__":
    s = Solution()
    print(s.minimumTotalDistance(robot = [0,4,6], factory = [[2,2],[6,2]])) # 4
    print(s.minimumTotalDistance(robot = [1,-1], factory = [[-2,1],[2,1]])) # 2