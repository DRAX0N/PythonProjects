"""
Valid Anagram
Easy
Topics
Company Tags
Hints
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_ord = [ord(ch) for ch in s]
        t_ord = [ord(ch) for ch in t]
        for letter in s_ord:
            if letter in t_ord:
                t_ord.remove(letter)
            else:
                return False
        return True

        """ Faster solution
        if len(s) == len(t):
            return sorted(s) == sorted(t)
        else:
            return False
        """
    
str1 = 'jam'
str2 = 'jar'
str3 = 'sam'
str4 = "msa"
sol = Solution()
result = sol.isAnagram(str3,str4)
print(result)