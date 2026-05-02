"""
1415. The k-th Lexicographical String of All Happy Strings of Length n
Medium
Topics
premium lock icon
Companies
Hint
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

 

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
 

Constraints:

1 <= n <= 10
1 <= k <= 100
"""

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def add_ch(temp):
            happy_l = ['a', 'b', 'c']
            letter_to_add = []
            for ch in happy_l:
                if ch != temp[-1]:
                    letter_to_add.append(ch)
            return letter_to_add

            
        # n - lenght of happy string
        # k - returned index
        happy_letters = ['a', 'b', 'c']
        #case_num = 3 * (2**(n-1))
        happy = []


        past_chs = ""
        
        for ch in happy_letters:
            curr_chars = [ch]
            while len(curr_chars[0]) != n:
                past_chs = curr_chars
                curr_chars = []
                for word in past_chs:
                    curr_letters = add_ch(word)
                    for letter in curr_letters:
                        word += letter
                        curr_chars.append(word)
                        word = word[:-1]
            happy += curr_chars

        return happy[k-1] if len(happy)>=k else ""
    
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Total number of happy strings of length n
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""
        ans = []
        prev = ""
        for i in range(n):
            # Try characters in lexicographical order
            for ch in ['a', 'b', 'c']:
                # Adjacent chars cannot be the same
                if ch == prev:
                    continue
                # Number of strings if we choose this character here
                remaining_len = n - i - 1
                cnt = 1 << remaining_len   # 2^remaining_len
                if k > cnt:
                    # Skip this whole block
                    k -= cnt
                else:
                    # This character belongs to the kth string
                    ans.append(ch)
                    prev = ch
                    break
        return "".join(ans)
    
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def backtrack(curr, last):

            if len(curr) == n:
                ans.append(curr)
                return

            for i in "abc":
                if i == last:
                    continue
                
                curr += i
                backtrack(curr, i)
                curr = curr[:-1]

                if len(ans) > k:
                    return
                
            return
        
        ans = []
        backtrack("", "")
        if len(ans) < k:
            return ""
        
        return ans[k - 1]  
    
if __name__ == "__main__":
    n = 3
    k = 9
    print(Solution().getHappyString(n, k)) # "cab"

    n = 1
    k = 4
    print(Solution().getHappyString(n, k)) # ""

    n = 1
    k = 3
    print(Solution().getHappyString(n, k)) # "c"