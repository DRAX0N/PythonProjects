"""
1345. Jump Game IV
Hard
Topics
premium lock icon
Companies
Hint
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
 

Constraints:

1 <= arr.length <= 5 * 104
-108 <= arr[i] <= 108
"""
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        from collections import defaultdict, deque
        graph = defaultdict(list)
        for i, v in enumerate(arr):
            graph[v].append(i)
        
        visited = set()
        q = deque([(0, 0)])
        while q:
            i, step = q.popleft()
            if i == len(arr) - 1:
                return step
            visited.add(i)
            for j in graph[arr[i]]:
                if j not in visited:
                    q.append((j, step + 1))
            graph[arr[i]] = []
            if i + 1 < len(arr) and i + 1 not in visited:
                q.append((i + 1, step + 1))
            if i - 1 >= 0 and i - 1 not in visited:
                q.append((i - 1, step + 1))


class Solution:
    '''
    Approach 1:
        * DFS - return min(dfs(i+1), dfs(i-1), for j in sameVal[i]: dfs(j))
    Approach 2:
        * MultiSource BFS from start
    Approach 3:
        * Bidirectional multisource bfs - from start and end explore the path with lesser nodes in the layer
    '''
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        valueToIdx = {}
        for i, num in enumerate(arr):
            if num in valueToIdx:
                valueToIdx[num].append(i)
            else:
                valueToIdx[num] = [i]

        visited = {0, n-1}
        jumps = 0
        start = set([0])
        end = set([n-1])
        while start:
            if len(start) > len(end):
                start, end = end, start
            nextQ = set()
            for i in start:
                             
                for j in valueToIdx[arr[i]]:
                    if j in end:
                        return jumps+1
                    
                    if j not in visited:
                        nextQ.add(j)
                        visited.add(j)
                # clear list to prevent redundant search
                valueToIdx[arr[i]].clear()

                if i-1 in end or i+1 in end:
                    return jumps+1
                
                if i-1 >= 0 and i-1 not in visited:
                    nextQ.add(i-1)
                    visited.add(i-1)
    
                if i+1 < n and i+1 not in visited:
                    nextQ.add(i+1)
                    visited.add(i+1)
            jumps+=1
            start = nextQ
        return -1
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.minJumps([100,-23,-23,404,100,23,23,23,3,404])) #3
    print(s.minJumps([7])) #0
    print(s.minJumps([7,6,9,6,9,6,9,7])) #1