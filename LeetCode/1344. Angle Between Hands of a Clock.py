"""
1344. Angle Between Hands of a Clock
Medium
Topics
premium lock icon
Companies
Hint
Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10-5 of the actual value will be accepted as correct.

 

Example 1:


Input: hour = 12, minutes = 30
Output: 165
Example 2:


Input: hour = 3, minutes = 30
Output: 75
Example 3:


Input: hour = 3, minutes = 15
Output: 7.5
 

Constraints:

1 <= hour <= 12
0 <= minutes <= 59
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #60 == 360 = 1 == 6
        #12 == 360 = 1 == 30
        hour_index = 30
        hours_start_angle = hour_index * hour
        #hours_end_angle = (hour_index * (hour+1)) if hour <12 else hour_index
        #print(hours_end_angle)
        minute_index = 6
        minutes_angle = minutes*minute_index

        hours_path = minutes_angle/360
        hours_angle = hours_start_angle+(hours_path*30)
        if hours_angle >=360:
            hours_angle-=360

        print(minutes_angle)
        print(hours_angle)
        #print("="*60)
        angle = abs(hours_angle-minutes_angle)
        if angle > 180:
            angle = min(angle, abs(angle-360))
        return angle 

if __name__ == "__main__":
    print(Solution().angleClock(12,30)) #165
    print(Solution().angleClock(3,30)) #75
    print(Solution().angleClock(3,15)) #7.5
    print(Solution().angleClock(1,57)) #7.5