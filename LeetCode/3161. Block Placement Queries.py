"""
161. Block Placement Queries
Hard
Topics
premium lock icon
Companies
Hint
There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.

You are given a 2D array queries, which contains two types of queries:

For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.

 

Example 1:

Input: queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]

Output: [false,true,true]

Explanation:



For query 0, place an obstacle at x = 2. A block of size at most 2 can be placed before x = 3.

Example 2:

Input: queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]

Output: [true,true,false]

Explanation:



Place an obstacle at x = 7 for query 0. A block of size at most 7 can be placed before x = 7.
Place an obstacle at x = 2 for query 2. Now, a block of size at most 5 can be placed before x = 7, and a block of size at most 2 before x = 2.
 

Constraints:

1 <= queries.length <= 15 * 104
2 <= queries[i].length <= 3
1 <= queries[i][0] <= 2
1 <= x, sz <= min(5 * 104, 3 * queries.length)
The input is generated such that for queries of type 1, no obstacle exists at distance x when the query is asked.
The input is generated such that there is at least one query of type 2.
"""



# You are given a 2D array queries, which contains two types of queries:

#For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
#For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
#Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.
#Hints:
#Let d[x] be the distance of the next obstacle after x.
#For each query of type 2, we just need to check if max(d[0], d[1], d[2], …d[x - sz]) > sz.
#Use segment tree to maintain d[x].

from typing import List, Optional

class FenwickTree:
    __slots__ = ('n', 'data')

    def __init__(self, n: int):
        self.n = n
        self.data = [0] * (n + 1)

    def update(self, index: int, delta: int = 1) -> None:
        i = index + 1
        while i <= self.n:
            self.data[i] += delta
            i += i & -i

    def query(self, index: int) -> int:
        i = index + 1
        total = 0
        while i > 0:
            total += self.data[i]
            i -= i & -i
        return total

    def find_by_prefix(self, prefix: int) -> int:
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)
        while bit_mask:
            next_idx = idx + bit_mask
            if next_idx <= self.n and self.data[next_idx] < prefix:
                prefix -= self.data[next_idx]
                idx = next_idx
            bit_mask >>= 1
        return idx

    def predecessor(self, index: int) -> Optional[int]:
        count = self.query(index)
        if count == 0:
            return None
        return self.find_by_prefix(count)

    def successor(self, index: int) -> Optional[int]:
        total = self.query(self.n - 1)
        count = self.query(index)
        if count == total:
            return None
        return self.find_by_prefix(count + 1)


class LazySegmentTree:
    __slots__ = ('n', 'size', 'maxseg', 'lazy', 'left')

    def __init__(self, n: int, init_end: int):
        size = 1
        while size < n:
            size <<= 1

        self.n = n
        self.size = size
        self.maxseg = [-10**9] * (2 * size)
        self.lazy = [None] * (2 * size)
        self.left = [0] * (2 * size)

        for i in range(size, size + n):
            self.left[i] = i - size
            self.maxseg[i] = init_end - (i - size)
        for i in range(size + n, 2 * size):
            self.left[i] = i - size
        for i in range(size - 1, 0, -1):
            self.left[i] = self.left[2 * i]
            self.maxseg[i] = max(self.maxseg[2 * i], self.maxseg[2 * i + 1])

    def _apply(self, node: int, value: int) -> None:
        self.maxseg[node] = value - self.left[node]
        self.lazy[node] = value

    def _push(self, node: int) -> None:
        lazy_val = self.lazy[node]
        if lazy_val is not None:
            self._apply(node * 2, lazy_val)
            self._apply(node * 2 + 1, lazy_val)
            self.lazy[node] = None

    def _pull(self, node: int) -> None:
        left = node * 2
        right = left + 1
        self.maxseg[node] = self.maxseg[left] if self.maxseg[left] > self.maxseg[right] else self.maxseg[right]

    def update_range(self, left: int, right: int, value: int, node: int = 1, node_left: int = 0, node_right: Optional[int] = None) -> None:
        if node_right is None:
            node_right = self.size - 1
        if left > node_right or right < node_left:
            return
        if left <= node_left and node_right <= right:
            self._apply(node, value)
            return
        self._push(node)
        mid = (node_left + node_right) // 2
        self.update_range(left, right, value, node * 2, node_left, mid)
        self.update_range(left, right, value, node * 2 + 1, mid + 1, node_right)
        self._pull(node)

    def query_max(self, left: int, right: int, node: int = 1, node_left: int = 0, node_right: Optional[int] = None) -> int:
        if node_right is None:
            node_right = self.size - 1
        if left > node_right or right < node_left:
            return -10**9
        if left <= node_left and node_right <= right:
            return self.maxseg[node]
        self._push(node)
        mid = (node_left + node_right) // 2
        left_max = self.query_max(left, right, node * 2, node_left, mid)
        right_max = self.query_max(left, right, node * 2 + 1, mid + 1, node_right)
        return left_max if left_max > right_max else right_max


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        max_x = 5 * 10 ** 4 + 1
        tree = LazySegmentTree(max_x, max_x)
        bit = FenwickTree(max_x)
        res: List[bool] = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                prev_obs = bit.predecessor(x - 1)
                start = 0 if prev_obs is None else prev_obs
                if start <= x - 1:
                    tree.update_range(start, x - 1, x)
                bit.update(x)
            else:
                x, sz = q[1], q[2]
                if x - sz < 0:
                    res.append(False)
                else:
                    res.append(tree.query_max(0, x - sz) >= sz)

        return res
#==================================================================================
class Solution:

    MAXX = 50000

    def __init__(self):
        self.seg = [0] * (4 * (self.MAXX + 1))

    def update(self, node, l, r, idx, val):
        if l == r:
            self.seg[node] = val
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)

        self.seg[node] = max(
            self.seg[2 * node],
            self.seg[2 * node + 1]
        )

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0

        if ql <= l and r <= qr:
            return self.seg[node]

        mid = (l + r) // 2

        return max(
            self.query(2 * node, l, mid, ql, qr),
            self.query(2 * node + 1, mid + 1, r, ql, qr)
        )

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        
        obstacles = SortedSet([0])

        # Build final obstacle configuration
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        pos = list(obstacles)

        # gap[pos[i]] = pos[i] - pos[i-1]
        for i in range(1, len(pos)):
            self.update(1,0,self.MAXX,pos[i],pos[i] - pos[i - 1])

        ans = []

        for i in range(len(queries) - 1, -1, -1):

            if queries[i][0] == 2:

                x = queries[i][1]
                sz = queries[i][2]

                idx = obstacles.bisect_right(x) - 1
                prev_obstacle = obstacles[idx]

                best = self.query(1,0,self.MAXX,0,prev_obstacle)
                best = max(best, x - prev_obstacle)

                ans.append(best >= sz)

            else:

                x = queries[i][1]

                idx = obstacles.index(x)
                left_pos = obstacles[idx - 1]

                # remove gap ending at x
                self.update(1,0,self.MAXX,x,0)

                if idx + 1 < len(obstacles):
                    right_pos = obstacles[idx + 1]
                    # merge gaps
                    self.update(1,0,self.MAXX,right_pos,right_pos - left_pos)

                obstacles.remove(x)

        return ans[::-1]
#==================================================================================
if __name__ == "__main__":
    s = Solution()
    print(s.getResults([[1,2],[2,3,3],[2,3,1],[2,2,2]]))  # [false,true,true]
    print(s.getResults([[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]))  # [true,true,false]
    print(s.getResults([[1,1],[1,11],[1,4],[1,8],[2,13,7]]))  # [false]
