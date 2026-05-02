"""
3600. Maximize Spanning Tree Stability with Upgrades
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer n, representing n nodes numbered from 0 to n - 1 and a list of edges, where edges[i] = [ui, vi, si, musti]:

ui and vi indicates an undirected edge between nodes ui and vi.
si is the strength of the edge.
musti is an integer (0 or 1). If musti == 1, the edge must be included in the spanning tree. These edges cannot be upgraded.
You are also given an integer k, the maximum number of upgrades you can perform. Each upgrade doubles the strength of an edge, and each eligible edge (with musti == 0) can be upgraded at most once.

The stability of a spanning tree is defined as the minimum strength score among all edges included in it.

Return the maximum possible stability of any valid spanning tree. If it is impossible to connect all nodes, return -1.

Note: A spanning tree of a graph with n nodes is a subset of the edges that connects all nodes together (i.e. the graph is connected) without forming any cycles, and uses exactly n - 1 edges.

 

Example 1:

Input: n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1

Output: 2

Explanation:

Edge [0,1] with strength = 2 must be included in the spanning tree.
Edge [1,2] is optional and can be upgraded from 3 to 6 using one upgrade.
The resulting spanning tree includes these two edges with strengths 2 and 6.
The minimum strength in the spanning tree is 2, which is the maximum possible stability.
Example 2:

Input: n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2

Output: 6

Explanation:

Since all edges are optional and up to k = 2 upgrades are allowed.
Upgrade edges [0,1] from 4 to 8 and [1,2] from 3 to 6.
The resulting spanning tree includes these two edges with strengths 8 and 6.
The minimum strength in the tree is 6, which is the maximum possible stability.
Example 3:

Input: n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0

Output: -1

Explanation:

All edges are mandatory and form a cycle, which violates the spanning tree property of acyclicity. Thus, the answer is -1.
 

Constraints:

2 <= n <= 105
1 <= edges.length <= 105
edges[i] = [ui, vi, si, musti]
0 <= ui, vi < n
ui != vi
1 <= si <= 105
musti is either 0 or 1.
0 <= k <= n
There are no duplicate edges.

"""

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        must_used_index = []
        can_be_used_index = []
        for index, connection in enumerate(edges):

            #if index>0:
            #    print("v = " + str(connection[0]))
            #    print("u -1 = " + str(edges[index-1][1]))
            if connection[3] == 1:
                must_used_index.append(index)
            elif index>0 and connection[0] == edges[index-1][1]:
                can_be_used_index.append(index)
            elif connection[0]<connection[1]:
                can_be_used_index.append(index)
            
        print("M")
        print(must_used_index)
        print("C")
        print(can_be_used_index)
        #strength upgrade
        strenght = []
        for index in can_be_used_index:
            strenght.append([edges[index][2], index])

        strenght.sort(reverse=True)
        for i in range(k):
             strenght[i][0] *= 2

        print(strenght)
#class DSU:
#    def __init__(self, n):
#        self.parent = list(range(n))
#        self.groups = n
#
#    def find(self, x):
#        if self.parent[x] != x:
#            self.parent[x] = self.find(self.parent[x])
#        return self.parent[x]
#
#    def unite(self, a, b):
#        pa = self.find(a)
#        pb = self.find(b)
#
#        if pa == pb:
#            return False
#
#        self.parent[pb] = pa
#        self.groups -= 1
#        return True
#
#
#class Solution:
#    def maxStability(self, n, edges, k):
#
#        dsu = DSU(n)
#
#        must_strength = []
#        opt_strength = []
#
#        must_edges = []
#        opt_edges = []
#
#        for e in edges:
#            if e[3] == 1:
#                must_edges.append(e)
#            else:
#                opt_edges.append(e)
#
#        for e in must_edges:
#            if dsu.unite(e[0], e[1]) == False:
#                return -1
#            must_strength.append(e[2])
#
#        opt_edges.sort(key=lambda x: 2*x[2], reverse=True)
#
#        for e in opt_edges:
#            if dsu.unite(e[0], e[1]) == True:
#                opt_strength.append(e[2])
#
#        if dsu.groups > 1:
#            return -1
#
#        opt_strength.sort()
#
#        used = 0
#        for i in range(len(opt_strength)):
#            if used == k:
#                break
#            opt_strength[i] *= 2
#            used += 1
#
#        res = float('inf')
#
#        for v in must_strength:
#            res = min(res, v)
#
#        for v in opt_strength:
#            res = min(res, v)
#
#        return res

if __name__ == "__main__":
    n = 3
    edges = [[0,1,2,1],[1,2,3,0]]
    k = 1
    print(Solution().maxStability(n, edges, k)) # 2
    #n = 3
    #edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]]
    #k = 2
    #print(Solution().maxStability(n, edges, k)) # 6
    #n = 3
    #edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]]
    #k = 0
    #print(Solution().maxStability(n, edges, k)) # -1