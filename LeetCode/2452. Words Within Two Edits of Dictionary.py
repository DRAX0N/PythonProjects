"""
2452. Words Within Two Edits of Dictionary
Medium
Topics
premium lock icon
Companies
Hint
You are given two string arrays, queries and dictionary. All words in each array comprise of lowercase English letters and have the same length.

In one edit you can take a word from queries, and change any letter in it to any other letter. Find all words from queries that, after a maximum of two edits, equal some word from dictionary.

Return a list of all words from queries, that match with some word from dictionary after a maximum of two edits. Return the words in the same order they appear in queries.

 

Example 1:

Input: queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
Output: ["word","note","wood"]
Explanation:
- Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
- Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
- It would take more than 2 edits for "ants" to equal a dictionary word.
- "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
Thus, we return ["word","note","wood"].
Example 2:

Input: queries = ["yes"], dictionary = ["not"]
Output: []
Explanation:
Applying any two edits to "yes" cannot make it equal to "not". Thus, we return an empty array.
 

Constraints:

1 <= queries.length, dictionary.length <= 100
n == queries[i].length == dictionary[j].length
1 <= n <= 100
All queries[i] and dictionary[j] are composed of lowercase English letters.
"""

from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        results = []
        
        for word in queries:
            for sentence in dictionary:
                sum = 0
                for letter in range(len(word)):
                    if word[letter] != sentence[letter]:
                        sum += 1
                if sum <= 2:
                    results.append(word)
                    break
        return results

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        
        for query in queries:
            for word in dictionary:
                if sum(1 for a, b in zip(query, word) if a != b) <= 2:
                    result.append(query)
                    break
        
        return result
    
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def _get_distance(s1,s2):
            cnt = 0
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    cnt+=1
                if cnt==3:
                    return False
            return True

            # zeros = dists.count(0)
            # return len(s1)-zeros
        good = []
        for query in queries:
            for d in dictionary:
                dist = _get_distance(query,d)
                if dist:
                    good.append(query)
                    break
        return good
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoEditWords(["word","note","ants","wood"], ["wood","joke","moat"])) #["word","note","wood"]
    print(solution.twoEditWords(["yes"], ["not"])) #[]







































        #result = []
#
        #for query in queries:
        #    for word in dictionary:
        #        if sum(1 for a, b in zip(query, word) if a != b) <= 2:
        #            result.append(query)
        #            break
#
        #return result
    