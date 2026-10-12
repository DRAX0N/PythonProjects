"""
1520. Maximum Number of Non-Overlapping Substrings
Hard
Topics
premium lock icon
Companies
Hint
Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

 

Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.
 

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.
"""

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        # Pierwsze i ostatnie wystąpienie każdego znaku.
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord("a")
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Tworzymy najmniejszy poprawny przedział dla każdego znaku.
        for char_idx in range(26):
            left = first[char_idx]

            if left == n:
                continue

            right = last[char_idx]
            i = left
            valid = True

            while i <= right:
                idx = ord(s[i]) - ord("a")

                # Znak występuje wcześniej poza aktualnym przedziałem,
                # więc nie da się utworzyć poprawnego substringa.
                if first[idx] < left:
                    valid = False
                    break

                right = max(right, last[idx])
                i += 1

            if valid:
                intervals.append((left, right))

        # Wybieramy przedziały kończące się najwcześniej.
        intervals.sort(key=lambda interval: interval[1])

        result = []
        previous_right = -1

        for left, right in intervals:
            if left > previous_right:
                result.append(s[left:right + 1])
                previous_right = right

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.maxNumOfSubstrings("adefaddaccc")) # ["e", "f", "ccc"]

    print(s.maxNumOfSubstrings("abbaccd")) # ["d", "bb", "cc"]