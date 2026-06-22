"""
3614. Process String with Special Operations II
Hard
Topics
premium lock icon
Companies
Hint
You are given a string s consisting of lowercase English letters and the special characters: '*', '#', and '%'.

You are also given an integer k.

Build a new string result by processing s according to the following rules from left to right:

If the letter is a lowercase English letter append it to result.
A '*' removes the last character from result, if it exists.
A '#' duplicates the current result and appends it to itself.
A '%' reverses the current result.
Return the kth character of the final string result. If k is out of the bounds of result, return '.'.

 

Example 1:

Input: s = "a#b%*", k = 1

Output: "a"

Explanation:

i	s[i]	Operation	Current result
0	'a'	Append 'a'	"a"
1	'#'	Duplicate result	"aa"
2	'b'	Append 'b'	"aab"
3	'%'	Reverse result	"baa"
4	'*'	Remove the last character	"ba"
The final result is "ba". The character at index k = 1 is 'a'.

Example 2:

Input: s = "cd%#*#", k = 3

Output: "d"

Explanation:

i	s[i]	Operation	Current result
0	'c'	Append 'c'	"c"
1	'd'	Append 'd'	"cd"
2	'%'	Reverse result	"dc"
3	'#'	Duplicate result	"dcdc"
4	'*'	Remove the last character	"dcd"
5	'#'	Duplicate result	"dcddcd"
The final result is "dcddcd". The character at index k = 3 is 'd'.

Example 3:

Input: s = "z*#", k = 0

Output: "."

Explanation:

i	s[i]	Operation	Current result
0	'z'	Append 'z'	"z"
1	'*'	Remove the last character	""
2	'#'	Duplicate the string	""
The final result is "". Since index k = 0 is out of bounds, the output is '.'.

 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters and special characters '*', '#', and '%'.
0 <= k <= 1015
The length of result after processing s will not exceed 1015.
"""

class Solution:
    def processStr(self, s: str, k: int) -> str:
        #temp = [ch for ch in s]
        #print(temp[-1::-1])
        result = ""
        for ch in s:
            if ord("a")<=ord(ch)<=ord("z"):
                result += ch
            elif ch == '*' and result != "":
                result = result[:-1]
            elif ch == '#':
                result += result
            elif ch == '%':
                result = result[::-1]
        return (result[k] if k<len(result) else ".")
    
class Solution:
    def processStr(self, s: str, k: int) -> str:
        #temp = [ch for ch in s]
        #print(temp[-1::-1])
        result = []
        for ch in s:
            if ord("a")<=ord(ch)<=ord("z"):
                result.append(ch)
            elif ch == '*' and result != "":
                result.pop()
            elif ch == '#':
                result += result
            elif ch == '%':
                result.reverse()

        return (result[k] if k<len(result) else ".")
    
class Solution:
    def processStr(self, s: str, k: int) -> str:
        N = len(s)
        sz = 0
        sizes = [0] * N  # O(N) pamięci zamiast O(2^n)
        
        # Krok 1: Przejście od przodu — obliczamy długość po każdej operacji
        for i, c in enumerate(s):
            if c == "*":
                if sz > 0:
                    sz -= 1
            elif c == "#":
                sz *= 2
            elif c == "%":
                pass  # odwrócenie nie zmienia długości
            else:
                sz += 1
            sizes[i] = sz
        
        # Jeśli k jest poza zasięgiem finalnej długości
        if k >= sz:
            return "."
        
        # Krok 2: Przejście od tyłu — cofamy się od k do początku
        for i in reversed(range(N)):
            c = s[i]
            sz = sizes[i]  # długość po operacji i
            
            if c == "*":
                continue  # pomijamy "*" w odwrotnej ścieżki
            elif c == "#":
                # Jeśli k jest w prawej połowie (kopii), mapujemy na lewą
                if k >= sz // 2:
                    k -= sz // 2
            elif c == "%":
                # Odwrócenie: nowy indeks = sz - 1 - k
                k = sz - 1 - k
            else:
                # To jest oryginalny znak
                if k == sz - 1:
                    return c
                sz -= 1  # zmniejszamy długość cofając się
        
        return "."
    
if __name__ == "__main__":
    print(Solution().processStr("a#b%*", 1)) #"a"
    print(Solution().processStr("cd%#*#",3)) #"d"
    print(Solution().processStr("z*#",0)) #"."