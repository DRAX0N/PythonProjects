"""
Longest Repeating Character Replacement
Medium
Topics
Company Tags
Hints
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.length
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_ord = [ord(ch)-ord("A") for ch in s]
        letter_counter = [0]*26
        last_pos_k = []
        l = 0
        r = 1
        target = 0
        k_counter = 0
        counter = 1
        max_sub = []
        while r < len(s):
            print("l = " + str(l))
            print("r = " + str(r))
            print(s[l:r+1])
            if s_ord[target] == s_ord[r]:
                counter += 1
                r += 1
            elif k == 0:
                max_sub.append(counter)
                l = r
                counter = 1
            elif k_counter < k:
                counter += 1
                k_counter += 1
                letter_counter[s_ord[r]] += 1
                last_pos_k.append(r)
                r += 1
            elif k_counter>= k:
                max_sub.append(counter)
                target = last_pos_k[0]
                l = target-k if k <=target else 0
                k_counter -= letter_counter[s_ord[l]]
                last_pos_k.pop(0)
                counter -= l
                r -= l
                #s_ord = s_ord[l:] + s_ord[0:l]
            print(s_ord)
            print("counter = " + str(counter))
            print("k_counter = " + str(k_counter))
        max_sub.append(counter)
        return max(max_sub)
    

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #s_ord = [ord(ch)-ord("A") for ch in s]
        #s_ord += s_ord[::-1]
        b = set(s)
        counter_list = []
        for target in b:
            counter = 0
            k_counter = 0
            l = 0
            r = 0
            while r < len(s):
                if target == s[r]:
                    counter +=1
                    r += 1
                elif target != s[r] and k_counter < k:
                    counter += 1
                    k_counter += 1
                    r += 1
                elif k_counter >= k:
                    counter_list.append(counter)
                    if s[l] != target:
                         k_counter -= 1
                    l += 1
                    counter -= 1
                else:
                    print("kurcze nie powinno mnie tu być")
            counter_list.append(counter)

        return max(counter_list)
                    
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
            max_freq = max(max_freq,count[s[right]])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len,right - left + 1)

        return max_len
     

if __name__ == '__main__':
    s = "XYYX"
    k = 2 #4

    #s = "AAABABB"
    #k = 1 #5

    #s="AABABBA"
    #k=1 #4
#
    #s="ABBB"
    #k=2

    new = Solution()
    print(new.characterReplacement(s,k))