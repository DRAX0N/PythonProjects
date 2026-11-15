"""
3841. Palindromic Path Queries in a Tree
Hard
Topics
premium lock icon
Companies
Hint
You are given an undirected tree with n nodes labeled 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.

You are also given a string s of length n consisting of lowercase English letters, where s[i] represents the character assigned to node i.

You are also given a string array queries, where each queries[i] is either:

"update ui c": Change the character at node ui to c. Formally, update s[ui] = c.
"query ui vi": Determine whether the string formed by the characters on the unique path from ui to vi (inclusive) can be rearranged into a palindrome.
Return a boolean array answer, where answer[j] is true if the jth query of type "query ui vi"​​​​​​​ can be rearranged into a palindrome, and false otherwise.

 

Example 1:

Input: n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]

Output: [true,false]

Explanation:

"query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.
"update 1 b": Update node 1 to 'b', now s = "abc".
"query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
Thus, answer = [true, false].

Example 2:

Input: n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]

Output: [false,false,true]

Explanation:

"query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form a palindrome. Thus, answer[0] = false.
"update 0 b": Update node 0 to 'b', now s = "bbca".
"query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
"update 3 a": Update node 3 to 'a', s = "bbca".
"query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form "bab", a palindrome. Thus, answer[2] = true.
Thus, answer = [false, false, true].

 

Constraints:

1 <= n == s.length <= 5 * 104
edges.length == n - 1
edges[i] = [ui, vi]
0 <= ui, vi <= n - 1
s consists of lowercase English letters.
The input is generated such that edges represents a valid tree.
1 <= queries.length <= 5 * 104​​​​​​​
queries[i] = "update ui c" or
queries[i] = "query ui vi"
0 <= ui, vi <= n - 1
c is a lowercase English letter.
"""

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        base = [0] * n          # początkowe pre[u]
        chars = [1 << (ord(c) - 97) for c in s]

        # iteracyjny DFS od korzenia 0
        timer = 0
        base[0] = chars[0]
        stack = [(0, 0, 0)]     # (węzeł, rodzic, indeks następnego dziecka)
        tin[0] = timer; timer += 1
        ptr = [0] * n
        up[0][0] = 0
        while stack:
            u, p, _ = stack[-1]
            if ptr[u] < len(adj[u]):
                v = adj[u][ptr[u]]
                ptr[u] += 1
                if v == p:
                    continue
                up[0][v] = u
                depth[v] = depth[u] + 1
                base[v] = base[u] ^ chars[v]
                tin[v] = timer; timer += 1
                stack.append((v, u, 0))
            else:
                tout[u] = timer - 1
                stack.pop()

        for k in range(1, LOG):
            prev, cur = up[k - 1], up[k]
            for v in range(n):
                cur[v] = prev[prev[v]]

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for k in range(LOG):
                if diff >> k & 1:
                    a = up[k][a]
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return up[0][a]

        # Fenwick XOR (indeksy 1..n+1): zakres XOR, zapytanie punktowe
        size = n + 2
        bit = [0] * (size + 1)

        def add(i: int, val: int) -> None:
            i += 1
            while i <= size:
                bit[i] ^= val
                i += i & -i

        def point(i: int) -> int:
            i += 1
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        # pre[u] = base[u] ^ point(tin[u])
        cur_chars = chars[:]
        res = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                x = int(parts[1])
                new = 1 << (ord(parts[2]) - 97)
                d = cur_chars[x] ^ new
                if d:
                    cur_chars[x] = new
                    add(tin[x], d)
                    add(tout[x] + 1, d)
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                pu = base[u] ^ point(tin[u])
                pv = base[v] ^ point(tin[v])
                mask = pu ^ pv ^ cur_chars[l]
                res.append(mask & (mask - 1) == 0)
        return res

if __name__ == "__main__":
    solution = Solution()
    n = 3
    edges = [[0,1],[1,2]]
    s = "aac"
    queries = ["query 0 2","update 1 b","query 0 2"]
    print(solution.palindromePath(n, edges, s, queries))  # Output: [True, False]

    n = 4
    edges = [[0,1],[0,2],[0,3]]
    s = "abca"
    queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]
    print(solution.palindromePath(n, edges, s, queries))  # Output: [False, False, True]