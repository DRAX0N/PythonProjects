"""
2840. Check if Strings Can be Made Equal With Operations II
Medium
Topics
premium lock icon
Companies
Hint
You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.

 

Example 1:

Input: s1 = "abcdba", s2 = "cabdab"
Output: true
Explanation: We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.
Example 2:

Input: s1 = "abe", s2 = "bea"
Output: false
Explanation: It is not possible to make the two strings equal.
 

Constraints:

n == s1.length == s2.length
1 <= n <= 105
s1 and s2 consist only of lowercase English letters.
"""
from collections import Counter
from collections import defaultdict
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # i < j and j%i == 0
        n = len(s1)
        index_to_change_even_s1 = []
        index_to_change_even_s2 = []
        index_to_change_odd_s1 = []
        index_to_change_odd_s2 = []
        for index in range(n):
            if s1[index] == s2[index]:
                continue
            elif index%2 == 0:
                index_to_change_even_s1.append(s1[index])
                index_to_change_even_s2.append(s2[index])
            else:
                index_to_change_odd_s1.append(s1[index])
                index_to_change_odd_s2.append(s2[index])

        index_to_change_even_s1.sort()  
        index_to_change_even_s2.sort()  
        index_to_change_odd_s1.sort()
        index_to_change_odd_s2.sort()

        return (index_to_change_even_s1 == index_to_change_even_s2 and index_to_change_odd_s1 == index_to_change_odd_s2)
                
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])
    
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        e1, o1 = defaultdict(int), defaultdict(int)
        e2, o2 = defaultdict(int), defaultdict(int)

        for i in range(n):
            if i % 2 == 0:
                e1[s1[i]] += 1
                e2[s2[i]] += 1
            else:
                o1[s1[i]] += 1
                o2[s2[i]] += 1
        
        return e1 == e2 and o1 == o2   

if __name__ == "__main__":
    s1 = "abcdba"
    s2 = "cabdab"
    print(Solution().checkStrings(s1, s2))# True
    s1 = "abe"
    s2 = "bea"
    print(Solution().checkStrings(s1, s2))# Fals