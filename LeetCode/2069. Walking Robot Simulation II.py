"""
2069. Walking Robot Simulation II
Medium
Topics
premium lock icon
Companies
Hint
A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".

The robot can be instructed to move for a specific number of steps. For each step, it does the following.

Attempts to move forward one cell in the direction it is facing.
If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
After the robot finishes moving the number of steps required, it stops and awaits the next instruction.

Implement the Robot class:

Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
void step(int num) Instructs the robot to move forward num steps.
int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".
 

Example 1:

example-1
Input
["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
Output
[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

Explanation
Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
robot.step(2);  // It moves two steps East to (2, 0), and faces East.
robot.step(2);  // It moves two steps East to (4, 0), and faces East.
robot.getPos(); // return [4, 0]
robot.getDir(); // return "East"
robot.step(2);  // It moves one step East to (5, 0), and faces East.
                // Moving the next step East would be out of bounds, so it turns and faces North.
                // Then, it moves one step North to (5, 1), and faces North.
robot.step(1);  // It moves one step North to (5, 2), and faces North (not West).
robot.step(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
                // Then, it moves four steps West to (1, 2), and faces West.
robot.getPos(); // return [1, 2]
robot.getDir(); // return "West"

 

Constraints:

2 <= width, height <= 100
1 <= num <= 105
At most 104 calls in total will be made to step, getPos, and getDir.
"""
from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.width = width-1
        self.height = height-1
        self.x = 0
        self.y = 0
        self.direction = 0
        self.directions = ["E", "N", "W", "S"]

    def step(self, num: int) -> None:
        for step in range(num):
                #(0,0)
            if ((self.x == 0 and self.y == 0 
                 and (self.direction % 4 == 2 or self.direction % 4 == 3)) 
                #(width,height)
                 or (self.x == self.width and self.y == self.height 
                 and (self.direction % 4 == 0 or self.direction % 4 == 1)
                #(width,0)
                 or (self.x == self.width and self.y == 0
                 and (self.direction % 4 == 0 or self.direction % 4 == 3))
                #(0,height)
                 or (self.x == 0 and self.y == self.height 
                 and (self.direction % 4 == 2 or self.direction % 4 == 1)))):
                self.direction += 1

            if self.direction % 4 == 0:
                self.x += 1
            elif self.direction % 4 == 1:
                self.y += 1
            elif self.direction % 4 == 2:
                self.x -= 1
            elif self.direction % 4 == 3:
                self.y -= 1

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        if self.direction % 4 == 0:
            return "East"
        elif self.direction % 4 == 1:
            return "North"
        elif self.direction % 4 == 2:
            return "West"
        elif self.direction % 4 == 3:
            return "South"

class Robot:

    def __init__(self, width: int, height: int):
        self.width = width-1
        self.height = height-1
        self.x = 0
        self.y = 0
        self.direction = 0
        self.directions = ["E", "N", "W", "S"]
        self.stat = 0

    def step(self, num: int) -> None:
            #(0,0)
        if ((self.x == 0 and self.y == 0 
             and (self.direction % 4 == 2 or self.direction % 4 == 3)) 
            #(width,height)
             or (self.x == self.width and self.y == self.height 
             and (self.direction % 4 == 0 or self.direction % 4 == 1)
            #(width,0)
             or (self.x == self.width and self.y == 0
             and (self.direction % 4 == 0 or self.direction % 4 == 3))
            #(0,height)
             or (self.x == 0 and self.y == self.height 
             and (self.direction % 4 == 2 or self.direction % 4 == 1)))):
            self.direction += 1
            self.stat = 1

        if self.direction % 4 == 0:
            if self.x + num <= self.width:
                self.x += num
            else:
                self.step_by_one(num)
        
        elif self.direction % 4 == 1:
            if self.y + num <= self.height:
                self.y += num
            else:
                self.step_by_one(num)
        elif self.direction % 4 == 2:
            if self.x - num >= 0:
                self.x -= num
            else:
                self.step_by_one(num)
        elif self.direction % 4 == 3:
            if self.y - num >= 0:
                self.y -= num
            else:
                self.step_by_one(num)
            

    def step_by_one(self, num: int) -> None:
        for step in range(num):
                #(0,0)
            if self.stat == 0:
                if ((self.x == 0 and self.y == 0 
                     and (self.direction % 4 == 2 or self.direction % 4 == 3)) 
                    #(width,height)
                     or (self.x == self.width and self.y == self.height 
                     and (self.direction % 4 == 0 or self.direction % 4 == 1)
                    #(width,0)
                     or (self.x == self.width and self.y == 0
                     and (self.direction % 4 == 0 or self.direction % 4 == 3))
                    #(0,height)
                     or (self.x == 0 and self.y == self.height 
                     and (self.direction % 4 == 2 or self.direction % 4 == 1)))):
                    self.direction += 1
            
            if self.direction % 4 == 0:
                self.x += 1
                self.stat = 0
            elif self.direction % 4 == 1:
                self.y += 1
                self.stat = 0
            elif self.direction % 4 == 2:
                self.x -= 1
                self.stat = 0
            elif self.direction % 4 == 3:
                self.y -= 1
                self.stat = 0

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        if self.direction % 4 == 0:
            return "East"
        elif self.direction % 4 == 1:
            return "North"
        elif self.direction % 4 == 2:
            return "West"
        elif self.direction % 4 == 3:
            return "South"

class Robot:
    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        self.x = 0
        self.y = 0
        self.dir_idx = 0  # 0:East, 1:North, 2:West, 3:South
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]

    def step(self, num: int) -> None:
        for _ in range(num):
            d = self.dir_idx % 4
            if (
                (self.x == 0 and self.y == 0 and d in (2, 3)) or
                (self.x == self.width and self.y == self.height and d in (0, 1)) or
                (self.x == self.width and self.y == 0 and d in (0, 3)) or
                (self.x == 0 and self.y == self.height and d in (1, 2))
            ):
                self.dir_idx += 1
                d = self.dir_idx % 4
            self.x += self.dx[d]
            self.y += self.dy[d]

    def getPos(self) -> list[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        dirs = ["East", "North", "West", "South"]
        return dirs[self.dir_idx % 4]
    
class Robot:
    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        self.x = 0
        self.y = 0
        self.dir_idx = 0
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]

    def step(self, num: int) -> None:
        x, y, dir_idx = self.x, self.y, self.dir_idx  # Lokalne!
        dx, dy = self.dx, self.dy
        w, h = self.width, self.height
        
        for _ in range(num):
            d = dir_idx % 4
            if (
                (x == 0 and y == 0 and d in (2, 3)) or
                (x == w and y == h and d in (0, 1)) or
                (x == w and y == 0 and d in (0, 3)) or
                (x == 0 and y == h and d in (1, 2))
            ):
                dir_idx += 1
                d = dir_idx % 4
            x += dx[d]
            y += dy[d]
        
        self.x = x
        self.y = y
        self.dir_idx = dir_idx

    def getPos(self) -> list[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        dirs = ["East", "North", "West", "South"]
        return dirs[self.dir_idx % 4]    

class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.dist  = 0
        self.per = 2 * (width + height) - 4
        self.notMoved = True

    def step(self, num: int) -> None:
        self.notMoved = False
        self.dist = (self.dist + num) %self.per 
        return 

    def getPos(self) -> list[int]:
        p, d, w, h = self.per, self.dist, self.width, self.height
        if   d == 0            : return [0, 0]
        elif d <  w            : return [d, 0]
        elif d <  w  + h - 1   : return [w - 1, d - w + 1]
        elif d <  2 * w + h-2  : return [p - h - d + 1, h -1 ]
        elif d                 : return [0, p - d]
        
    def getDir(self) -> str:
        if self.notMoved : return "East"
        
        w, h = self.width, self.height
        if   self.dist == 0            : return "South"
        elif self.dist < w             : return "East"
        elif self.dist < w + h - 1     : return "North"
        elif self.dist < 2 * w + h - 2 : return "West"
        elif self.dist                 : return "South"
        
class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        # Total steps to complete one full loop
        self.perimeter = 2 * (width + height - 2)
        # 1D position tracking
        self.pos = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        # Modulo arithmetic completely bypasses the simulation
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> list[int]:
        p = self.pos
        
        # 1. Bottom edge (Moving East)
        if p < self.w:
            return [p, 0]
        # 2. Right edge (Moving North)
        elif p < self.w + self.h - 1:
            return [self.w - 1, p - (self.w - 1)]
        # 3. Top edge (Moving West)
        elif p < 2 * self.w + self.h - 2:
            # Start at right edge, subtract the steps moved along the top
            return [(self.w - 1) - (p - (self.w + self.h - 2)), self.h - 1]
        # 4. Left edge (Moving South)
        else:
            # Start at top edge, subtract the steps moved down the left side
            # Fun fact: mathematically this simplifies beautifully to self.perimeter - p
            return [0, self.perimeter - p]

    def getDir(self) -> str:
        p = self.pos
        
        # The Edge Case: (0, 0)
        if p == 0:
            return "South" if self.moved else "East"
            
        if p < self.w:
            return "East"
        elif p < self.w + self.h - 1:
            return "North"
        elif p < 2 * self.w + self.h - 2:
            return "West"
        else:
            return "South"  
# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

if __name__ == "__main__":
    # Example 1
    robot = Robot(6, 3)
    robot.step(2)
    robot.step(2)
    print(robot.getPos())  # Output: [4, 0]
    print(robot.getDir())  # Output: "East"
    robot.step(2)
    robot.step(1)
    robot.step(4)
    print(robot.getPos())  # Output: [1, 2]
    print(robot.getDir())  # Output: "West"