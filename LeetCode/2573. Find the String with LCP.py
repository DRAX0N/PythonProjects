"""
2573. Find the String with LCP
Hard
Topics
premium lock icon
Companies
Hint
We define the lcp matrix of any 0-indexed string word of n lowercase English letters as an n x n grid such that:

lcp[i][j] is equal to the length of the longest common prefix between the substrings word[i,n-1] and word[j,n-1].
Given an n x n matrix lcp, return the alphabetically smallest string word that corresponds to lcp. If there is no such string, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "aabd" is lexicographically smaller than "aaca" because the first position they differ is at the third letter, and 'b' comes before 'c'.

 

Example 1:

Input: lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
Output: "abab"
Explanation: lcp corresponds to any 4 letter string with two alternating letters. The lexicographically smallest of them is "abab".
Example 2:

Input: lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
Output: "aaaa"
Explanation: lcp corresponds to any 4 letter string with a single distinct letter. The lexicographically smallest of them is "aaaa". 
Example 3:

Input: lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
Output: ""
Explanation: lcp[3][3] cannot be equal to 3 since word[3,...,3] consists of only a single letter; Thus, no answer exists.
 

Constraints:

1 <= n == lcp.length == lcp[i].length <= 1000
0 <= lcp[i][j] <= n
"""
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [""] * n
        current = ord("a")

        for i in range(n):
            if not word[i]:
                if current > ord("z"):
                    return ""
                word[i] = chr(current)
                for j in range(i + 1, n):
                    if lcp[i][j]:
                        word[j] = word[i]
                current += 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] != word[j]:
                    if lcp[i][j]:
                        return ""
                else:
                    if i == n - 1 or j == n - 1:
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""

        return "".join(word)
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:  
        n = len(lcp)
        curr = 1
        letters = [0]*n

        for i in range(n):
            if letters[i]: 
                continue
            if curr > 26: 
                return ""
            
            for j in range(i, n):
                if lcp[i][j]: 
                    letters[j] = curr
            curr += 1

        for i in range(n):
            for j in range(n):
                if letters[i] != letters[j]: 
                    expected = 0
                else: 
                    expected = (lcp[i+1][j+1] if i < n - 1 and j < n-1 else 0) +1
                if expected != lcp[i][j]: 
                    return ""

        res = ''
        for num in letters:
            res += chr(ord('a') - 1 + num)

        return res

if __name__ == "__main__":
    print(Solution().findTheString(lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]])) # "abab"
    print(Solution().findTheString(lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]])) # "aaaa"
    print(Solution().findTheString(lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]])) # ""