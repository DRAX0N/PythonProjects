"""
2751. Robot Collisions
Hard
Topics
premium lock icon
Companies
Hint
There are n 1-indexed robots, each having a position on a line, health, and movement direction.

You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.

All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.

If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.

Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final health of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.

Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.

Note: The positions may be unsorted.

 
 

Example 1:



Input: positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"
Output: [2,17,9,15,10]
Explanation: No collision occurs in this example, since all robots are moving in the same direction. So, the health of the robots in order from the first robot is returned, [2, 17, 9, 15, 10].
Example 2:



Input: positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"
Output: [14]
Explanation: There are 2 collisions in this example. Firstly, robot 1 and robot 2 will collide, and since both have the same health, they will be removed from the line. Next, robot 3 and robot 4 will collide and since robot 4's health is smaller, it gets removed, and robot 3's health becomes 15 - 1 = 14. Only robot 3 remains, so we return [14].
Example 3:



Input: positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"
Output: []
Explanation: Robot 1 and robot 2 will collide and since both have the same health, they are both removed. Robot 3 and 4 will collide and since both have the same health, they are both removed. So, we return an empty array, [].
 

Constraints:

1 <= positions.length == healths.length == directions.length == n <= 105
1 <= positions[i], healths[i] <= 109
directions[i] == 'L' or directions[i] == 'R'
All values in positions are distinct
"""

from typing import List

#class Solution:
#    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
#        def  check_eq_pos(temp):
#            to_fight = {}
#            to_del = set()
#            for i in range(1, len(temp)):
#                print(temp[i][0])
#                if temp[i][0] == temp[i-1][0]:
#                    if temp[i][0] in to_fight.keys():
#                        to_fight[temp[i][0]].append([temp[i][1],i])
#                        to_fight[temp[i-1][0]].append([temp[i-1][1],i-1])
#                        to_del.add(i-1)
#                        to_del.add(i)
#                    else:
#                        to_fight[temp[i][0]] = [[temp[i-1][1],i-1]]
#                        to_fight[temp[i][0]].append([temp[i][1],i])
#                        to_del.add(i-1)
#                        to_del.add(i)
#            print(to_fight)
#            #for key in to_fight.keys():
#            #    safe_index = to_fight[key].index(max(to_fight[key]))
#            #    to_del.pop(to_fight[key][safe_index][1])
#            #    if 
#            return to_fight
#
#        robots = [[positions[index],healths[index],directions[index]] for index in range(len(healths))]
#        print(robots)
#        #temp = healths
#        while True:
#            for index in range(len(robots)):
#                if robots[index][2] == "R":
#                    robots[index][0]  += 1
#                else:
#                    robots[index][0] -= 1
#            robots.sort()
#            for i in range(1, len(robots)):
#                if robots[i][0] == robots[i-1][0]:
#                    if 
#            #to_del = check_eq_pos(robots)
#            #break
#            #if to_del != []:
#            #    robots.pop


                
#from dataclasses import dataclass
#from typing import List
#
#@dataclass
#class Robot:
#    index: int
#    position: int
#    health: int
#    direction: str
#
#class Solution:
#    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
#        robots = sorted([Robot(i, positions[i], healths[i], directions[i]) 
#                        for i in range(len(positions))], 
#                       key=lambda x: x.position)
#        stack: List[Robot] = []
#        
#        for robot in robots:
#            if robot.direction == 'R':
#                stack.append(robot)
#                continue
#            
#            # Kolizje z 'R' na stosie
#            while stack and stack[-1].direction == 'R' and robot.health > 0:
#                if stack[-1].health == robot.health:
#                    stack.pop()
#                    robot.health = 0
#                elif stack[-1].health < robot.health:
#                    stack.pop()
#                    robot.health -= 1
#                else:
#                    stack[-1].health -= 1
#                    robot.health = 0
#            
#            if robot.health > 0:
#                stack.append(robot)
#        
#        stack.sort(key=lambda r: r.index)
#        return [r.health for r in stack]

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        positions = sorted([(pos, i) for i, pos in enumerate(positions)])
        stack = []
        for p, i in positions:
            if directions[i] == "R":
                stack.append(i)
                continue
            while stack:
                j = stack.pop()
                if healths[i] > healths[j]:
                    healths[i] -= 1
                    healths[j] = 0
                elif healths[i] < healths[j]:
                    healths[j] -= 1
                    healths[i] = 0
                    stack.append(j)
                    break
                else:
                    healths[i] = healths[j] = 0
                    break
        return [h for h in healths if h > 0]
"""
# Brute Force Code
# What Ask
# - Return an array containing the health of the remaining robots in the order they were given in the input after no further collisions can occur.
class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str):
        # number of robots
        n = len(positions)
        # combine robot information into single list each robot will store : [position, health, direction, original_index]
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
        # sort robots by position this allows us the check collsions between adjacent robots
        robots.sort()
        # boolean array to track whether a robot is alive
        alive = [True] * n
        # flag to keep repeating collision checks until no more collisions occur
        changed = True
        while changed:
            changed = False
            # iterate through adjacent robots
            for i in range(len(robots) - 1):
                # skip robots that are already removed
                if not alive[i] or not alive[i + 1]:
                    continue
                # unpack robot data
                # - robot move i position
                position_1, health_1, direction_1, idx_1 = robots[i]
                # - robot move i + 1 position
                position_2, health_2, direction_2, idx_2 = robots[i + 1]
                # collision occurs only when left robots moves right and right robot moves left
                if direction_1 == 'R' and direction_2 == 'L':
                    changed = True
                    # robot i has more health than survives
                    if health_1 > health_2:
                        # surviving robot losses one health
                        robots[i][1] -= 1
                        # robot i + 1 dies
                        alive[i + 1] = False
                    # robot i + 1 has more health than survives 
                    elif health_1 < health_2:
                        # surviving robot losses one health
                        robots[i + 1][1] -= 1
                        # robot i  dies
                        alive[i] = False
                    # both have equal health so both die
                    else:
                        alive[i] = False
                        alive[i + 1] = False
        # collect survivors robots store original_index, remaining_health
        result = []
        for i in range(len(robots)):
            if alive[i]:
                result.append((robots[i][3], robots[i][1]))
        # sort surviours by original input order
        result.sort()
        # return only health values
        return [health for _, health in result]

# Time Complexity : O(logN)
# Space Complexity : O(N^2)
"""

# Optimal Code
# What Ask
# - Return an array containing the health of the remaining robots in the order they were given in the input after no further collisions can occur.
class Solution:
    def survivedRobotsHealths(self,positions:list[int], healths:list[int],directions:str):
        # map each robots position to its index in the input arrays
        index_map = {p: i for i, p in enumerate(positions)}
        # stack to store indices of robots moving to the right
        stack = []
        # process robots in order of increasing position
        for p in sorted(positions):
            i = index_map[p]
            if directions[i] == "R":
                # robot moving right push its index to stack
                stack.append(i)
            else:
                # robot moving left to check for collisions
                while stack and directions[stack[-1]] == "R" and healths[i] > 0:
                    # robot moving right the might collide
                    i2 = stack.pop()
                    if healths[i] > healths[i2]:
                        # left robot wins -> right robot dies
                        healths[i2] = 0
                        # loses 1 helath after collision
                        healths[i] -= 1
                    elif healths[i] < healths[i2]:
                        # right robot wins -> left robot dies
                        healths[i] = 0
                        # right robot losses 1 health
                        healths[i2] -= 1
                        # still alive, push back to stack
                        stack.append(i2)
                    else:
                        # equal health -> both robots die
                        healths[i] = healths[i2] = 0
                # if left robot is still alive after all possible collisions keep it
                if healths[i] > 0:
                    stack.append(i)
        # return the healths of all surviving robots (health > 0)
        return [h for h in healths if h  > 0]

# Time Complexity : O(logN)
# Space Complexity : O(N)

if __name__ == "__main__":
    s = Solution()
    print(s.survivedRobotsHealths([5,4,3,2,1], [2,17,9,15,10], "RRRRR"))#[2,17,9,15,10]
    print(s.survivedRobotsHealths([3,5,2,6], [10,10,15,12], "RLRL"))#[14]
    print(s.survivedRobotsHealths([1,2,5,6], [10,10,11,11], "RLRL"))#[]