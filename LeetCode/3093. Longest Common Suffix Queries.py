"""
3093. Longest Common Suffix Queries
Hard
Topics
premium lock icon
Companies
Hint
You are given two arrays of strings wordsContainer and wordsQuery.

For each wordsQuery[i], you need to find a string from wordsContainer that has the longest common suffix with wordsQuery[i]. If there are two or more strings in wordsContainer that share the longest common suffix, find the string that is the smallest in length. If there are two or more such strings that have the same smallest length, find the one that occurred earlier in wordsContainer.

Return an array of integers ans, where ans[i] is the index of the string in wordsContainer that has the longest common suffix with wordsQuery[i].

 

Example 1:

Input: wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]

Output: [1,1,1]

Explanation:

Let's look at each wordsQuery[i] separately:

For wordsQuery[0] = "cd", strings from wordsContainer that share the longest common suffix "cd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
For wordsQuery[1] = "bcd", strings from wordsContainer that share the longest common suffix "bcd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
For wordsQuery[2] = "xyz", there is no string from wordsContainer that shares a common suffix. Hence the longest common suffix is "", that is shared with strings at index 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
Example 2:

Input: wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]

Output: [2,0,2]

Explanation:

Let's look at each wordsQuery[i] separately:

For wordsQuery[0] = "gh", strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.
For wordsQuery[1] = "acbfgh", only the string at index 0 shares the longest common suffix "fgh". Hence it is the answer, even though the string at index 2 is shorter.
For wordsQuery[2] = "acbfegh", strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.
 

Constraints:

1 <= wordsContainer.length, wordsQuery.length <= 104
1 <= wordsContainer[i].length <= 5 * 103
1 <= wordsQuery[i].length <= 5 * 103
wordsContainer[i] consists only of lowercase English letters.
wordsQuery[i] consists only of lowercase English letters.
Sum of wordsContainer[i].length is at most 5 * 105.
Sum of wordsQuery[i].length is at most 5 * 105.
"""
# If we reverse the strings, the problem changes to finding the longest common prefix.
# Build a Trie, each node is a letter and only saves the best word’s index in each node, based on the criteria.

from typing import List

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.best_index = -1

        root = TrieNode()

        def update_best_index(node: TrieNode, candidate_index: int) -> None:
            if node.best_index == -1:
                node.best_index = candidate_index
                return

            current_index = node.best_index
            current_len = len(wordsContainer[current_index])
            candidate_len = len(wordsContainer[candidate_index])

            if candidate_len < current_len or (candidate_len == current_len and candidate_index < current_index):
                node.best_index = candidate_index

        for i, word in enumerate(wordsContainer):
            update_best_index(root, i)
            node = root
            for c in reversed(word):
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
                update_best_index(node, i)

        ans = []
        for word in wordsQuery:
            node = root
            best_index = node.best_index
            for c in reversed(word):
                if c not in node.children:
                    break
                node = node.children[c]
                best_index = node.best_index
            ans.append(best_index)

        return ans

from bisect import bisect_left
from math import inf

class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        Non-Trie solution.

        Idea:
        1) Reverse every word.
           Longest common suffix becomes longest common prefix.

        2) Sort reversed container words lexicographically.
           Strings with the same prefix become a contiguous block.

        3) For each query:
           - reverse it
           - find the maximum LCP with any container word
             using only the neighbors around its insertion point
           - then find the whole prefix block of that length
           - among that block, pick the shortest word
             (and if tie, the earliest index)

        We use a segment tree to answer:
            "which container word is best in a sorted interval?"
        where "best" means:
            smaller length first,
            then smaller original index.
        """

        # ------------------------------------------------------------
        # 1) Reverse all container words and keep:
        #    - reversed string
        #    - original length
        #    - original index
        #
        # We sort by reversed string, because suffix matching on the
        # original words becomes prefix matching on reversed words.
        # ------------------------------------------------------------
        container = []
        for idx, w in enumerate(wordsContainer):
            container.append((w[::-1], len(w), idx))

        container.sort(key=lambda x: x[0])

        rev_words = [x[0] for x in container]

        # best_info[i] = (length, original_index)
        # This is what we want to minimize inside a prefix block.
        best_info = [(x[1], x[2]) for x in container]

        n = len(container)

        # ------------------------------------------------------------
        # 2) Segment tree for range minimum on (length, index)
        #    Python tuple comparison works exactly how we want:
        #       (len1, idx1) < (len2, idx2)
        #    means smaller length first, then smaller index.
        # ------------------------------------------------------------
        size = 1
        while size < n:
            size *= 2

        seg = [(inf, inf)] * (2 * size)

        for i in range(n):
            seg[size + i] = best_info[i]

        for i in range(size - 1, 0, -1):
            seg[i] = min(seg[2 * i], seg[2 * i + 1])

        def query(l, r):
            """
            Return the best (length, index) in container[l..r].
            """
            l += size
            r += size
            ans = (inf, inf)

            while l <= r:
                if l % 2 == 1:
                    ans = min(ans, seg[l])
                    l += 1
                if r % 2 == 0:
                    ans = min(ans, seg[r])
                    r -= 1
                l //= 2
                r //= 2

            return ans

        # ------------------------------------------------------------
        # Helper: longest common prefix length of a and b
        # ------------------------------------------------------------
        def lcp(a, b):
            i = 0
            limit = min(len(a), len(b))
            while i < limit and a[i] == b[i]:
                i += 1
            return i

        # ------------------------------------------------------------
        # 3) For each query:
        #
        #    - reverse it
        #    - find the maximum LCP with any container word
        #      (it is enough to check the two neighbors around
        #       the insertion position in sorted order)
        #    - then find the full block of words having that prefix
        #    - query the segment tree on that interval to pick the best
        # ------------------------------------------------------------
        ans = []

        for q in wordsQuery:
            rq = q[::-1]

            # insertion position of rq in the sorted reversed container
            pos = bisect_left(rev_words, rq)

            # maximum LCP with any word is achieved by one of the
            # two neighbors around the insertion point
            best_l = 0
            if pos < n:
                best_l = max(best_l, lcp(rev_words[pos], rq))
            if pos > 0:
                best_l = max(best_l, lcp(rev_words[pos - 1], rq))

            # prefix of the query that must match the answer
            prefix = rq[:best_l]

            # all container words with this prefix form a contiguous block
            # in the sorted reversed array
            left = bisect_left(rev_words, prefix)
            right = bisect_left(rev_words, prefix + "{") - 1
            # '{' comes right after 'z' in ASCII,
            # so prefix + '{' is the first string that is strictly larger
            # than any lowercase string starting with prefix.

            # pick the best candidate in that whole block:
            #   1) smallest length
            #   2) earliest original index
            _, idx = query(left, right)
            ans.append(idx)

        return ans

if __name__ == "__main__":
    s = Solution()
    s.stringIndices(["abcd","bcd","xbcd"], ["cd","bcd","xyz"]) # [1, 1, 1]
    s.stringIndices(["abcdefgh","poiuygh","ghghgh"], ["gh","acbfgh","acbfegh"]) # [2, 0, 2]