"""
3121. Count the Number of Special Characters II
Medium
Topics
premium lock icon
Companies
Hint
You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.

 

Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

There are no special characters in word.

Example 3:

Input: word = "AbBCab"

Output: 0

Explanation:

There are no special characters in word.

 

Constraints:

1 <= word.length <= 2 * 105
word consists of only lowercase and uppercase English letters.
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        numbers = [ord(ch)-ord("A") for ch in word]
        temp = set()
        added = []
        counter = 0
        for n in numbers:
            
            if n >=32:
                if n in temp and n-32 in temp:
                    if n-32 in added:
                        counter -= 1
                        added.remove(n-32)
                    else:
                        continue
                temp.add(n)
            else:
                if n in temp and n+32 in temp:
                    continue
                if n+32 in temp:
                    counter += 1
                    added.append(n)
                temp.add(n)
        return counter
    
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt = 0
        for i in range(65, 91):
            fui = 0
            lli = 0
            uLetter = chr(i)
            if uLetter in word:
                fui = word.find(uLetter)      # fui = first uppercase letter index
                lLetter = uLetter.lower()
                if lLetter in word:
                    lli = word.rfind(lLetter)  # lli = last lowercase letter index
                    if fui - lli > 0:
                        cnt += 1
        return cnt
    
if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSpecialChars("aaAbcBC")) #3
    print(s.numberOfSpecialChars("abc")) #0
    print(s.numberOfSpecialChars("AbBCab")) #0