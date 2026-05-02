"""
You are given a string s consisting of lowercase English letters.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.

 

Example 1:

Input: s = "abbac"

Output: 4

Explanation:

The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

Example 2:

Input: s = "zzabccy"

Output: 4

Explanation:

The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​

Example 3:

Input: s = "aba"

Output: 2

Explanation:

​​​​​​​One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""

class Solution:
    def __init__(self):
        pass
    #def longestBalanced(self, s: str) -> int:
    #    s_len = len(s)
    #    def differnece(text):
    #        subs = {}
    #        for l in text:
    #            subs[l] = subs.get(l, 0) + 1
    #        values = list(subs.values())
    #        freq = values[0]
    #        return all(v == freq for v in values)
    #        #subs = {}
    #        #for letter in text:
    #        #    if letter in subs:
    #        #        subs[letter] += 1
    #        #    else:
    #        #        subs[letter] = 1
    #        #n = 0
    #        #for v in subs.values():
    #        #    if n == 0:
    #        #        n = v
    #        #    elif n!=v:
    #        #        return False
    #        #return True
#
    #    for length in range(s_len, 0, -1):
    #        start = s_len - length
    #        for begin in range(start+1):
    #            sub = s[begin:begin + length]
    #            if differnece(sub):
    #                print(sub)
    #                print(length)
    #                return length 
    #            
    #    #result = False
    #    #reduce = 1        
    #    #while s_len>=1:
    #    #    
    #    #    for n in range(reduce):
    #    #        word = ""
    #    #        for l in s[n:s_len+n]:
    #    #            word += l                   
    #    #        result = differnece(word)
    #    #        if result:
    #    #            print(word)
    #    #            print(len(word))
    #    #            return word
    #    #            break
    #    #    if result:
    #    #        break
    #    #    else:
    #    #        s_len -= 1
    #    #        reduce += 1
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        # Transform char -> int
        s = [ord(char) - ord('a') for char in s]
        print(s)
        result = 0
        for l in range(n):
            if n - l <= result:  # Early exit, can't be bigger
                break

            cnt = [0] * 26  # Counts of every char
            uniq = maxfreq = 0  # Number of uniq chars and maximum frequency
            for r in range(l, n):
                i = s[r]

                uniq += cnt[i] == 0  # There was no this char before => one more uniq
                cnt[i] += 1
                if cnt[i] > maxfreq:  # Update max frequency
                    maxfreq = cnt[i]

                # Check if all uniq chars have maxfreq frequency then update the result
                cur = r - l + 1
                if uniq * maxfreq == cur and cur > result:
                    result = cur
        print(result)
        return result 

s0 = "abc"
s1 = "aacczbacg"
s2 = "zzabccy"
s3 ="hfifijiggfijjhihhjihggihjhfijfhgiihfhijfihjgiiijjifjgijjifhgfjgigfhjigjgjfghghfggfihfifihhjhfhhgjghggfjhjghijiihhifghifijgjihjgjjijigjfhfggiigjgffgghfggjhiigghhiigfhjifjfgjfhifjhhgfjfghijhijggjfgjjjiggijjhhhiijfiijfijjfghiifjighfijjhjiihjhiifhghjjjjjfjjgjfjjfghhfhijfhhhiggjgfgiffjhhfgfhiihjfgfhgjjggfigfifjghhjhgfihggigffhigfhifjjggjjhhfjjfihjhhhihjighgfgggjfifggffhijfiihjifgfjigjfifjjffjgfhgigjggjiihfhijgjiijgiffijigjjijhfjigggiiggjfhgghjhj"
s4 = 'a'
new = Solution()
new.longestBalanced(s1)