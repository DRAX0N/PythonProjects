"""
Daily Temperatures
Medium
Topics
Company Tags
Hints
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
Constraints:

1 <= temperatures.length <= 1000.
1 <= temperatures[i] <= 100
"""

#class Solution:
#    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#        result = [0]*len(temperatures)
#        high_temp =  False
#        for index, temp in enumerate(temperatures):
#            for temp_after in temperatures[index+1::]:
#                if temp < temp_after:
#                    result[index] += 1
#                    high_temp = True
#                    break
#                elif temp >= temp_after:
#                    result[index] += 1
#                else:
#                    continue
#            if not high_temp:
#                result[index] = 0
#            high_temp = False
#        return result

#class Solution:
#    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#        stack = []
#        result = [0] * len(temperatures)
#        for day, temp in enumerate(temperatures):
#            print(stack)
#            while(len(stack) != 0 and temp > stack[-1][0]):
#                    _, past_day = stack.pop(-1)
#                    result[past_day] = day - past_day
#            stack.append((temp, day))
#                
#        return result
    
#class Solution:
#    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#        stack = []
#        result = [0] * len(temperatures)
#        for day, temp in enumerate(temperatures):
#            if day>0 and temp > stack[day-1][1]:
#                
#                
#            stack.append((day,temp))
#
#                
#        return result
    

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):   
            while stack and temp > stack[-1][0]:
                _, stack_index = stack.pop()
                result[stack_index] = index - stack_index
            stack.append([temp,index]) 
        return result
    

if __name__ == "__main__":
    temperatures=[30,38,30,36,35,40,28]
    new = Solution()

    print(new.dailyTemperatures(temperatures))