"""
3120. Count the Number of Special Characters I
Easy
Topics
premium lock icon
Companies
Hint
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.

 

Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters in word are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

No character in word appears in uppercase.

Example 3:

Input: word = "abBCab"

Output: 1

Explanation:

The only special character in word is 'b'.

 

Constraints:

1 <= word.length <= 50
word consists of only lowercase and uppercase English letters.
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        numbers = [ord(ch)-ord("A") for ch in word]
        temp = set()
        counter = 0
        for n in numbers:
            
            if n >=32:
                if n in temp and n-32 in temp:
                    continue
                elif n-32 in temp:
                    counter += 1
                temp.add(n)
            else:
                if n in temp and n+32 in temp:
                    continue
                if n+32 in temp:
                    counter += 1
                temp.add(n)
        return counter
    
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # a-z:97,122
        # A-Z:65,90
        res = [0]*26
        seen_upper, seen_lower = set(), set()
        for c in word:
            if ord(c)>96 and c not in seen_lower:
                res[97-ord(c)]+= 1
                seen_lower.add(c)
            if ord(c)<91 and c not in seen_upper:
                res[65-ord(c)]+= 1
                seen_upper.add(c)
        ans = 0
        for num in res:
            if num==2:
                ans+=1
        return ans
    
if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSpecialChars("aaAbcBC"))  # Output: 3
    print(s.numberOfSpecialChars("abc"))       # Output: 0
    print(s.numberOfSpecialChars("abBCab"))    # Output: 1