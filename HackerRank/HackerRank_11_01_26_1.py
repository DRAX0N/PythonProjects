import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    solution = ""
    position_to_change = []
    for num in range(0, len(s)):
        if num == 0 and (s[num].isalpha() or s[num].isdigit()):
            position_to_change.append(num)
        elif (s[num].isalpha() or s[num].isdigit()) and (not s[num-1].isdigit()  and not s[num-1].isalpha()):
            position_to_change.append(num)
    workspace = [letter for letter in s]
    for i in position_to_change:
        workspace[i] = workspace[i].upper()
    for l in workspace:
        solution += l
    return solution

    
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()
    s = "hello   world  lol"

    result = solve(s)
    print(result)
    #fptr.write(result + '\n')

    #fptr.close()