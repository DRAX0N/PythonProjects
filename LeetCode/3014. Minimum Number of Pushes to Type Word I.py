"""

Code
Testcase
Test Result
Test Result
3014. Minimum Number of Pushes to Type Word I
Easy
Topics
premium lock icon
Companies
Hint
You are given a string word containing distinct lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.


 

Example 1:


Input: word = "abcde"
Output: 5
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.
Example 2:


Input: word = "xycdefghij"
Output: 12
Explanation: The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> two pushes on key 2
"c" -> one push on key 3
"d" -> two pushes on key 3
"e" -> one push on key 4
"f" -> one push on key 5
"g" -> one push on key 6
"h" -> one push on key 7
"i" -> one push on key 8
"j" -> one push on key 9
Total cost is 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = 12.
It can be shown that no other mapping can provide a lower cost.
 

Constraints:

1 <= word.length <= 26
word consists of lowercase English letters.
All letters in word are distinct.
"""
from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        # 1. Policz częstotliwość każdej litery
        freq = Counter(word)
        
        # 2. Posortuj częstotliwości malejąco
        sorted_freqs = sorted(freq.values(), reverse=True)
        
        # 3. Oblicz całkowity koszt
        total_pushes = 0
        for i, count in enumerate(sorted_freqs):
            # i // 8 + 1 daje: 1 dla i=0..7, 2 dla i=8..15, 3 dla i=16..23, 4 dla i=24..25
            pushes_per_char = i // 8 + 1
            total_pushes += count * pushes_per_char
        
        return total_pushes
    
class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = [word.count(chr(ord('a') + i)) for i in range(26)] 
        arr = sorted(counts, reverse=True)
        total = 0
        for group, i in enumerate(range(0, len(arr), 8), start=1):
            total += sum(arr[i:i+8]) * group

        return total
    
if __name__ == "__main__":
    solution = Solution()
    word1 = "abcde"
    print(solution.minimumPushes(word1))  # Output: 5

    word2 = "xycdefghij"
    print(solution.minimumPushes(word2))  # Output: 12

    word3 = "amrvxnhsewkoipjyuclgtdbfq"
    print(solution.minimumPushes(word3))  # Output: 52