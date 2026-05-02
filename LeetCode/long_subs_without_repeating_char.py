"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    #def lengthOfLongestSubstring(self, s: str) -> int:
    #    s_len = len(s)
    #    if s_len <= 1:
    #        return s_len 
    #        
    #    s2_len = len(s)
    #    n_list = [ord(character) for character in s]
#
    #    counter = [0]*128
    #    uniqe = 0
    #    max_len = 0
    #    n = 0
    #    current = True
    #    while current:
    #        for index in range(s_len):
    #            counter[n_list[index+n]] += 1
    #            if max_len>s_len:
    #                current = False
    #            elif counter[n_list[index+n]] == 1:
    #                uniqe += 1
    #                if uniqe > max_len:
    #                    max_len = uniqe
    #            elif counter[n_list[index+n]] > 1:
    #                counter = [0]*128
    #                uniqe = 0
#
    #        s_len -= 1
    #        n+=1
    #        counter = [0]*128
    #        uniqe = 0
    #        if s_len == 1:
    #            current = False
    #    return max_len
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        last_pos = [-1] * 128  # ostatnia pozycja znaku (ASCII)
        left = 0               # lewa granica bieżącego okna (substringu)
        max_len = 0

        for right, ch in enumerate(s):
            code = ord(ch)

            # jeśli znak był już w oknie, przesuwamy lewą granicę za jego poprzednie wystąpienie
            if last_pos[code] >= left:
                left = last_pos[code] + 1

            # aktualizujemy ostatnią pozycję znaku
            last_pos[code] = right

            # długość aktualnego okna [left, right]
            cur_len = right - left + 1
            if cur_len > max_len:
                max_len = cur_len

        return max_len

#st = "jbpnbwwd"
st = "abbcaad"
new = Solution()
result = new.lengthOfLongestSubstring(st)
print(result)

