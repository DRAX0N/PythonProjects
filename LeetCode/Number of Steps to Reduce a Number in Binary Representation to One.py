"""
1404. Number of Steps to Reduce a Number in Binary Representation to One
Medium
Topics
premium lock icon
Companies
Hint
Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

 

Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  
Example 2:

Input: s = "10"
Output: 1
Explanation: "10" corresponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  
Example 3:

Input: s = "1"
Output: 0
 

Constraints:

1 <= s.length <= 500
s consists of characters '0' or '1'
s[0] == '1'
"""
# all operation string
#class Solution:
#    def numSteps(self, s: str) -> int:
#        counter = 0
#        bit_1_set = False
#        while s != "1":
#            if s[-1]=="1":
#                for i in range(len(s)-2,-1,-1):
#                    if s[i]=='0':
#                        if i>0 and i<len(s)-1:
#                            s=s[:i]+'1'+s[i+1:]
#                        bit_1_set = True       
#                        break 
#                if bit_1_set==False:
#                    s = "1"+(len(s)*"0")
#                else:
#                   bit_1_set = False
#                s=s[:len(s)-1] + '0'
#            else: 
#                s=s[:len(s)-1]
#            counter += 1  
#        return counter
    
# all operation int
class Solution:
    def numSteps(self, s: str) -> int:
        number = int(s,2)
        counter = 0
        while number != 1:
            if number%2 == 0:
                number = number//2
            else:
                number += 1
            counter += 1
        return counter

if __name__ == "__main__":
    #s = "1101" #output 6
    #s = "11000" #output 6
    #s = "1110" #output 5
    #s = "11001" #output 8
    s = "1111011110000011100000110001011011110010111001010111110001"
    print(Solution().numSteps(s)) 