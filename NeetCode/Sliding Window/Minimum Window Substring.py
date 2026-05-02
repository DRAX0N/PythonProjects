"""
Minimum Window Substring
Hard
Topics
Company Tags
Hints
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"
Example 3:

Input: s = "x", t = "xy"

Output: ""
Constraints:

1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def letter_check(d_count):
            for key in d_count.keys():
                if d_count[key] > 0:
                    return False
            return True

        if len(t) > len(s):
            return ""
        
        s_count = {}
        t_count = {}

        for ch in s:
            s_count[ch] = s_count.get(ch, 0) + 1
        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1
        #print(t_count)
        for ch in t:
            if ch not in s:
                return ""
            elif t_count[ch] > s_count[ch]:
                return ""
        if len(t) == len(s):
            return s
        
        min_len = (float("inf"), "")
        #print(min_len)
        l = 0
        r = 0
        if s[l] in t:
            t_count[s[l]] -= 1
            if letter_check(t_count):
                return s[l]

        while r <= len(s)-1:
            if letter_check(t_count):
                #print("==============")
                #print("l = "+str(l))
                #print("r = "+str(r))
                min_len = min(min_len, (len(s[l:r+1]), s[l:r+1]))
                if s[l] in t:
                    t_count[s[l]] += 1
                l += 1
                continue
            
            r += 1
            if r <= len(s)-1 and s[r] in t and r>l:
                t_count[s[r]] -= 1
        if letter_check(t_count):
            min_len = min(min_len, (len(s[l:r+1]), s[l:r+1]))
        #print(min_len)
        return (min_len)[1]

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        have = 0
        need_count = len(need)

        best_len = float("inf")
        best_l = 0
        best_r = 0

        l = 0
        for r in range(len(s)):
            ch = s[r]
            if ch in need:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] == need[ch]:
                    have += 1

            while have == need_count:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l
                    best_r = r

                left_ch = s[l]
                if left_ch in need:
                    window[left_ch] -= 1
                    if window[left_ch] < need[left_ch]:
                        have -= 1
                l += 1

        return "" if best_len == float("inf") else s[best_l:best_r + 1]

if __name__ == "__main__":
    s = Solution()
    #print(s.minWindow("OUZODYXAZV", "XYZ"))#"YXAZ"
    #print(s.minWindow("xyz", "xyz")) #"xyz"
    #print(s.minWindow("x", "xy"))#  ""

    s1="ADOBECODEBANC"
    t1="ABC"
    print(s.minWindow(s1, t1)) #"ADOBEC"
