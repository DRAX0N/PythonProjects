"""
Car Fleet
Medium
Topics
Company Tags
Hints
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

Example 1:

Input: target = 10, position = [1,4], speed = [3,2]

Output: 1
Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

Example 2:

Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

Output: 3
Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

Constraints:

n == position.length == speed.length.
1 <= n <= 1000
0 < target <= 1000
0 < speed[i] <= 100
0 <= position[i] < target
All the values of position are unique.
"""

#OLD SOLUTION 15/22 TC passed
"""
        position_speed = []
        for i in range(len(position)):
            position_speed.append([position[i], speed[i]])
        position_speed.sort(reverse=True)
        print(position_speed)

        target_reach = False
        stack = []
        while position_speed != []:
            for index, [position, speed] in enumerate(position_speed):
                print("pozycja, prędkość = " + str(position_speed[index]))
                position_speed[index][0] += speed
                if position_speed[index][0] >=position_speed[index-1][0] and index > 0:
                    position_speed.pop(index)
                elif position_speed[index][0] >= target:
                    target_reach_index = index
                    target_reach = True
            if target_reach:
                stack.append(position_speed[target_reach_index])
                position_speed.pop(target_reach_index)
                target_reach = False
            print("position_speed = " + str(position_speed))
            print("stack = " + str(stack))
                

        
        return len(stack)
"""
from ast import List

# solucja do gry planszowej
#class Solution:
#    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#        position_speed = []
#        for i in range(len(position)):
#            if position[i] < target:
#                position_speed.append([position[i], speed[i]])
#        position_speed.sort(reverse=True)
#        print(position_speed)
#        
#        item_to_delete = []
#        target_reach = False
#        stack = []
#        i = 1
#        while position_speed != []:
#            print("\n")
#            print("KOLEJKA!!! = " + str(i) + "\n")
#            for index, [position, speed] in enumerate(position_speed):
#                
#                position_speed[index][0] += speed
#                if position_speed[index][0] >=position_speed[0][0] and index > 0:
#                    print("Usuwam " + str(position_speed[index]) + " bo dogania " + str(position_speed[index-1]))
#                    item_to_delete.append(index)
#                elif position_speed[index][0] >= target and target_reach == False:
#                    target_reach_index = index
#                    item_to_delete.append(target_reach_index)
#                    target_reach = True
#                
#                print("pozycja, prędkość = " + str(position_speed[index]))
#            if target_reach:
#                stack.append(position_speed[target_reach_index])
#                #position_speed.pop(target_reach_index)
#                target_reach = False
#            if item_to_delete != []:
#                for index in sorted(item_to_delete, reverse=True):
#                    position_speed.pop(index)
#                item_to_delete = []
#
#            i+=1
#            print("position_speed = " + str(position_speed))
#            print("stack = " + str(stack))
#
#
#                
#        print("\n")
#        print("ODPOWIEDZ")
#        
#        return len(stack)

""" AI NEET CODE SOLUTION
        position_speed = []
        for i in range(len(position)):
            if position[i] < target:
                # Calculate time to reach target as a float to avoid precision issues
                time_to_reach = (target - position[i]) / speed[i]
                position_speed.append([position[i], time_to_reach])
        
        # Sort by starting position descending (closest to target first)
        position_speed.sort(key=lambda x: x[0], reverse=True)
        
        if not position_speed:
            return 0
            
        stack = []
        for pos, time in position_speed:
            # If stack is empty or this car takes longer than the fleet in front,
            # it starts a new fleet.
            if not stack or time > stack[-1]:
                stack.append(time)
            # Otherwise, it catches up and becomes part of the existing fleet
                
        return len(stack)
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = []
        for i in range(len(position)):
            if position[i] < target:
                position_speed.append([position[i], speed[i]])
        position_speed.sort(reverse=True)

        time_to_reach = []
        for pos, spd in position_speed:
            time_to_reach.append((target-pos)/spd)
        print(time_to_reach)

        stack = [time_to_reach[0]]
        for time in time_to_reach[1::]:  
            if time>stack[-1]:
                stack.append(time)          

        return len(stack)



        


                
if __name__ == "__main__":
    target=31
    position=[5,26,18,25,29,21,22,12,19,6]
    speed=[7,6,6,4,3,4,9,7,6,4]
    new = Solution()


    print(new.carFleet(target, position, speed))