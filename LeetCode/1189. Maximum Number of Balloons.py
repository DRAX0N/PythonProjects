"""
1189. Maximum Number of Balloons
Easy
Topics
premium lock icon
Companies
Hint
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
 

Note: This question is the same as 2287: Rearrange Characters to Make Target String.
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        core = "balon"
        l_o_multi = 2
        core_cnt = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0
        }

        for ch in text:
            if ch in core:
                core_cnt[ch] += 1

        min_wor = float("inf")
        for key in core_cnt.keys():
            if key in ["l", "o"]: 
                min_wor = min(core_cnt[key]//l_o_multi, min_wor)
            else:
                min_wor = min(core_cnt[key], min_wor)

        return min_wor
    
from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = defaultdict(int)
        word = "balloon"
        for t in text:
            if t in word:
                d[t] +=1
        
        if any(t not in d for t in word):
            return 0
        else:
            return min(d['b']//1, d['a']//1, d['l']//2, d['o']//2, d['n']//1)

if __name__ == "__main__":
    print(Solution().maxNumberOfBalloons("nlaebolko")) #1
    print(Solution().maxNumberOfBalloons("loonbalxballpoon")) #2
    print(Solution().maxNumberOfBalloons("leetcode")) #0