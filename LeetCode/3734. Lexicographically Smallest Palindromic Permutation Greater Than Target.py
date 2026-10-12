"""
3734. Lexicographically Smallest Palindromic Permutation Greater Than Target
Hard
Topics
premium lock icon
Companies
Hint
You are given two strings s and target, each of length n, consisting of lowercase English letters.

Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

 

Example 1:

Input: s = "baba", target = "abba"

Output: "baab"

Explanation:

The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
The lexicographically smallest permutation that is strictly greater than target is "baab".
Example 2:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
None of them is lexicographically strictly greater than target. Therefore, the answer is "".
Example 3:

Input: s = "abc", target = "abb"

Output: ""

Explanation:

s has no palindromic permutations. Therefore, the answer is "".

Example 4:

Input: s = "aac", target = "abb"

Output: "aca"

Explanation:

The only palindromic permutation of s is "aca".
"aca" is strictly greater than target. Therefore, the answer is "aca".
 

Constraints:

1 <= n == s.length == target.length <= 300
s and target consist of only lowercase English letters.
"""
from collections import Counter
from string import ascii_lowercase

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        freq = Counter(s)
        
        def check() -> bool:
            return all(v >= 0 for v in freq.values())

        center = ''
        for x, v in freq.items():
            if v % 2 == 0: continue
            if center: return ""
            center = x
            freq[x] -= 1

        sz = len(s)
        half = sz // 2
        for i, w in enumerate(target[:half]):
            freq[w] -= 2

        if check():
            head = target[:half]
            tail = center + head[::-1]
            if tail > target[half:]:
                return head + tail

        for i in range(half - 1, -1, -1):
            w = target[i]
            freq[w] += 2
            if not check(): continue

            for j in range(ord(w) - ord('a') + 1, 26):
                x = ascii_lowercase[j]
                if freq[x] == 0: continue

                freq[x] -= 2
                result = list(target[:i + 1])
                result[i] = x

                for x in ascii_lowercase:
                    result.extend(x * (freq[x] // 2))

                tail = result[::-1]
                result.append(center)
                result += tail

                return ''.join(result)

        return ""

if __name__ == "__main__":
    solution = Solution()
    print(solution.lexPalindromicPermutation("baba", "abba"))  # Output: "baab"
    print(solution.lexPalindromicPermutation("baba", "bbaa"))  # Output: ""
    print(solution.lexPalindromicPermutation("abc", "abb"))    # Output: ""
    print(solution.lexPalindromicPermutation("aac", "abb"))    # Output: "aca"
    print(solution.lexPalindromicPermutation("z", "z"))         # Output: ""