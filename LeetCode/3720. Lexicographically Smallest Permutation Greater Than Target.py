"""
3720. Lexicographically Smallest Permutation Greater Than Target
Medium
Topics
premium lock icon
Companies
Hint
You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

 

Example 1:

Input: s = "abc", target = "bba"

Output: "bca"

Explanation:

The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
The lexicographically smallest permutation that is strictly greater than target is "bca".
Example 2:

Input: s = "leet", target = "code"

Output: "eelt"

Explanation:

The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
The lexicographically smallest permutation that is strictly greater than target is "eelt".
Example 3:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
None of them is lexicographically strictly greater than target. Therefore, the answer is "".
 

Constraints:

1 <= s.length == target.length <= 300
s and target consist of only lowercase English letters.
"""

from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        def can_form_greater(counts, t):
            total = sum(counts.values())
            m = len(t)
            if total < m:
                return False
            if total > m:
                return True
            # total == m: check if largest permutation > t
            largest_chars = []
            for ch in sorted(counts.keys(), reverse=True):
                if counts[ch] > 0:
                    largest_chars.extend([ch] * counts[ch])
            largest = "".join(largest_chars)
            return largest > t

        if len(s) != len(target):
            if len(s) < len(target):
                return ""
            counts = Counter(s)
            smallest_chars = []
            for ch in sorted(counts.keys()):
                smallest_chars.extend([ch] * counts[ch])
            smallest = "".join(smallest_chars)
            return smallest if smallest > target else ""

        counts = Counter(s)

        # If no permutation of s can be > target, return ""
        if not can_form_greater(counts, target):
            return ""

        n = len(s)
        res = []
        equal_prefix = True

        for i in range(n):
            if not equal_prefix:
                # Already greater: fill with smallest available chars
                for ch in sorted(counts.keys()):
                    if counts[ch] > 0:
                        res.append(ch)
                        counts[ch] -= 1
                        if counts[ch] == 0:
                            del counts[ch]
                        break
                continue

            # equal_prefix is True: must keep prefix >= target prefix
            found = False
            for ch in sorted(counts.keys()):
                if counts[ch] == 0:
                    continue
                if ch < target[i]:
                    continue
                if ch > target[i]:
                    # Prefix becomes strictly greater
                    res.append(ch)
                    counts[ch] -= 1
                    if counts[ch] == 0:
                        del counts[ch]
                    equal_prefix = False
                    found = True
                    break
                else:  # ch == target[i]
                    # Try to stay equal, check feasibility of suffix
                    counts[ch] -= 1
                    if counts[ch] == 0:
                        del counts[ch]
                    if can_form_greater(counts, target[i+1:]):
                        res.append(ch)
                        equal_prefix = True
                        found = True
                        break
                    else:
                        # Restore count and try next character
                        counts[ch] = counts.get(ch, 0) + 1

            if not found:
                return ""

        return "".join(res)
    
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # Consume as much of target's prefix as the multiset allows.
        p = 0
        while p < n:
            c = ord(target[p]) - 97
            if cnt[c] == 0:
                break
            cnt[c] -= 1
            p += 1

        i = p
        while i >= 0:
            if i < n:
                t = ord(target[i]) - 97
                pick = -1
                for c in range(t + 1, 26):
                    if cnt[c] > 0:
                        pick = c
                        break
                if pick >= 0:
                    cnt[pick] -= 1
                    tail = ''.join(chr(97 + c) * cnt[c] for c in range(26))
                    cnt[pick] += 1
                    return target[:i] + chr(97 + pick) + tail
            i -= 1
            if i >= 0:
                cnt[ord(target[i]) - 97] += 1
        return ""
    
if __name__ == "__main__":
    solution = Solution()
    s = "abc"
    target = "bba"
    print(solution.lexGreaterPermutation(s, target))  # Output: "bca"

    s = "leet"
    target = "code"
    print(solution.lexGreaterPermutation(s, target))  # Output: "eelt"

    s = "baba"
    target = "bbaa"
    print(solution.lexGreaterPermutation(s, target))  # Output: ""