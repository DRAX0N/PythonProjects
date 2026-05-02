"""
Longest Substring Without Repeating Characters
Medium
Topics
Company Tags
Hints
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
Constraints:

0 <= s.length <= 1000
s may consist of printable ASCII characters.
"""
class Solution:
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
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        counter = 0
        n_list = [ord(ch) - ord("a") for ch in s]
        #print([ord(ch) - ord("a") for ch in s])
        temp_list = []

        while r<len(n_list):
            #print([ord(ch) - ord("a") for ch in s])
            #print(n_list)
            if n_list[r] in temp_list:
                #print("value = " + str(r-l))
                l = n_list.index(n_list[r],l,r)
                index = n_list.pop(l)
                #print("value = " + str(index))
                temp_list = n_list[l:r]
            else:
                temp_list.append(n_list[r])
                r+=1
            counter = max(len(temp_list), counter)
            #print(temp_list)
            #print(counter)

        return counter


if __name__ == '__main__':
    #s = "zxyzxyz" #3
    #s = "xxxx" #1
    #s = "pwwkew" #3
    #s = "thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert" #17 [19, 7, 4, 16, 20, 8, 2, 10, 1, 17, 14, 22, 13, 5, 14, 23, 9, 20, 12, 15, 18, 14, 21, 4, 17, 19, 7, 4, 11, 0, 25, 24, 3, 14, 6, 19, 7, 4, 16, 20, 8, 2, 10, 1, 17, 14, 22, 13, 5, 14, 23, 9, 20, 12, 15, 18, 14, 21, 4, 17, 19]
    s = "bprkpqlbtqpqphr" #7 [1, 15, 17, 10, 15, 16, 11, 1, 19, 16, 15, 16, 15, 7, 17]
    new = Solution()
    print(new.lengthOfLongestSubstring(s))