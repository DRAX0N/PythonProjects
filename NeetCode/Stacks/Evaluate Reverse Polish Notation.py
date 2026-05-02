"""
Evaluate Reverse Polish Notation
Medium
Topics
Company Tags
Hints
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].
"""
# old wrong soulution
#class Solution:
#    def evalRPN(self, tokens: List[str]) -> int:
#        signs = ["+","-","*","/"]
#        num_list = []
#        result = 0
#        for element in tokens:
#            if element in signs:
#                if element == "+":
#                    for n in num_list[1::]:
#                        result = num_list[0] + n
#                elif element == "-":
#                    for n in num_list[1::]:
#                        result = num_list[0] - n
#                elif element == "*":
#                    for n in num_list[1::]:
#                        result = num_list[0] * n
#                elif element == "/":
#                    for n in num_list[1::]:
#                        result = num_list[0] - n  
#                num_list = []
#                num_list.append(result)
#            else:
#                num_list.append(int(element))
#            
#        return result
    
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = ["+","-","*","/"]
        num_list = []
        for element in tokens:
            if element in signs:
                if element == "+":
                    print(element)
                    num_list[-2] = num_list[-2] + num_list[-1]
                    num_list.pop()
                elif element == "-":
                    print(element)
                    num_list[-2] = num_list[-2] - num_list[-1]
                    num_list.pop()   
                elif element == "*":
                    print(element)
                    num_list[-2] = num_list[-2] * num_list[-1]
                    num_list.pop()  
                elif element == "/":
                    print(element)
                    num_list[-2] = int(num_list[-2] / num_list[-1])
                    num_list.pop()  
            else:
                num_list.append(int(element))
            print(num_list)
        return num_list[0]
if __name__ == "__main__":
    nums=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    new = Solution()

    print(new.evalRPN(nums))