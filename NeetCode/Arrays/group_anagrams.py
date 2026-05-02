"""
Group Anagrams
Medium
Topics
Company Tags
Hints
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def equal_strings(s1, s2):
            s1_ord = [ord(ch) for ch in s1]
            s2_ord = [ord(ch) for ch in s2]
            for letter in s1_ord:
                if letter in s2_ord:
                    s2_ord.remove(letter)
                else:
                    return False
            return True
        
        result = []
        solution = []
        added = False
        for text in strs:
            
            for text_list in solution:
                if len(text) == len(text_list[0]):
                    if equal_strings(text, text_list[0]):
                        text_list.append(text)
                        added = True
                        break
                    else:
                        added = False
            print(text)
            if not(added):
                solution.append([text])
                added = False
            print(solution)
        
        return solution
                    
##class Solution:
##    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
##        hashmap = {}
##        for i in strs:
##            a = ''.join(sorted(i))
##            hashmap[a] = hashmap.get(a, []) + [i]
##        return list(hashmap.values())
        
    
text = ["act","pots","tops","cat","stop","hat"]
solution = Solution()
result = solution.groupAnagrams(text)
print(result)