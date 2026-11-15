"""
3863. Minimum Operations to Sort a String
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s consisting of lowercase English letters.

In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.

Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.

 

Example 1:

Input: s = "dog"

Output: 1

Explanation:​​​​​​​

Sort substring "og" to "go".
Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.
Example 2:

Input: s = "card"

Output: 2

Explanation:

Sort substring "car" to "acr", so s = "acrd".
Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order. Thus, the answer is 2.
Example 3:

Input: s = "gf"

Output: -1

Explanation:

It is impossible to sort s under the given constraints. Thus, the answer is -1.
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""

class Solution:
    def minOperations(self, s: str) -> int:
        # Już posortowany niemalejąco
        if all(a <= b for a, b in pairwise(s)):
            return 0

        # Dla długości 2 nie można wybrać całego stringa,
        # a sortowanie pojedynczego znaku nic nie zmienia.
        if len(s) == 2:
            return -1

        mn, mx = min(s), max(s)

        # Pierwszy znak to minimum albo ostatni to maksimum:
        # sortujemy pozostałą część jednym ruchem.
        if s[0] == mn or s[-1] == mx:
            return 1

        # Jeśli min lub max występuje w środku,
        # najpierw doprowadzamy go na brzeg, potem sortujemy resztę.
        if any(c in (mn, mx) for c in s[1:-1]):
            return 2

        # Najgorszy przypadek: min i max są tylko na końcach,
        # a środek nie zawiera żadnego z nich.
        return 3

if __name__ == "__main__":
    s = "dog"
    solution = Solution()
    print(solution.minOperations(s))  # Output: 1

    s = "card"
    print(solution.minOperations(s))  # Output: 2

    s = "gf"
    print(solution.minOperations(s))  # Output: -1