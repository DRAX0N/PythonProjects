"""

Code
Testcase
Test Result
Test Result
3501. Maximize Active Section with Trade II
Hard
Topics
premium lock icon
Companies
Hint
You are given a binary string s of length n, where:

'1' represents an active section.
'0' represents an inactive section.
You can perform at most one trade to maximize the number of active sections in s. In a trade, you:

Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
Additionally, you are given a 2D array queries, where queries[i] = [li, ri] represents a substring s[li...ri].

For each query, determine the maximum possible number of active sections in s after making the optimal trade on the substring s[li...ri].

Return an array answer, where answer[i] is the result for queries[i].

Note

For each query, treat s[li...ri] as if it is augmented with a '1' at both ends, forming t = '1' + s[li...ri] + '1'. The augmented '1's do not contribute to the final count.
The queries are independent of each other.
 

Example 1:

Input: s = "01", queries = [[0,1]]

Output: [1]

Explanation:

Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

Example 2:

Input: s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]]

Output: [4,3,1,1]

Explanation:

Query [0, 3] → Substring "0100" → Augmented to "101001"
Choose "0100", convert "0100" → "0000" → "1111".
The final string without augmentation is "1111". The maximum number of active sections is 4.

Query [0, 2] → Substring "010" → Augmented to "10101"
Choose "010", convert "010" → "000" → "111".
The final string without augmentation is "1110". The maximum number of active sections is 3.

Query [1, 3] → Substring "100" → Augmented to "11001"
Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

Query [2, 3] → Substring "00" → Augmented to "1001"
Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

Example 3:

Input: s = "1000100", queries = [[1,5],[0,6],[0,4]]

Output: [6,7,2]

Explanation:

Query [1, 5] → Substring "00010" → Augmented to "1000101"
Choose "00010", convert "00010" → "00000" → "11111".
The final string without augmentation is "1111110". The maximum number of active sections is 6.

Query [0, 6] → Substring "1000100" → Augmented to "110001001"
Choose "000100", convert "000100" → "000000" → "111111".
The final string without augmentation is "1111111". The maximum number of active sections is 7.

Query [0, 4] → Substring "10001" → Augmented to "1100011"
Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.

Example 4:

Input: s = "01010", queries = [[0,3],[1,4],[1,3]]

Output: [4,4,2]

Explanation:

Query [0, 3] → Substring "0101" → Augmented to "101011"
Choose "010", convert "010" → "000" → "111".
The final string without augmentation is "11110". The maximum number of active sections is 4.

Query [1, 4] → Substring "1010" → Augmented to "110101"
Choose "010", convert "010" → "000" → "111".
The final string without augmentation is "01111". The maximum number of active sections is 4.

Query [1, 3] → Substring "101" → Augmented to "11011"
Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.

 

Constraints:

1 <= n == s.length <= 105
1 <= queries.length <= 105
s[i] is either '0' or '1'.
queries[i] = [li, ri]
0 <= li <= ri < n
"""
from typing import List 

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')
        
        type_arr = []
        start = []
        end_idx = []
        
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            type_arr.append(int(s[i]))
            start.append(i)
            end_idx.append(j - 1)
            i = j
            
        N = len(type_arr)
        
        pos_to_seg = [0] * n
        for idx in range(N):
            for j in range(start[idx], end_idx[idx] + 1):
                pos_to_seg[j] = idx
                
        ans = [0] * N
        for idx in range(1, N - 1):
            if type_arr[idx] == 1:
                ans[idx] = (end_idx[idx - 1] - start[idx - 1] + 1) + (end_idx[idx + 1] - start[idx + 1] + 1)
                
        log_table = [0] * (N + 1)
        for idx in range(2, N + 1):
            log_table[idx] = log_table[idx // 2] + 1
            
        K = log_table[N] + 1
        st = [[0] * N for _ in range(K)]
        
        for idx in range(N):
            st[0][idx] = ans[idx]
            
        for j in range(1, K):
            for idx in range(N - (1 << j) + 1):
                st[j][idx] = max(st[j - 1][idx], st[j - 1][idx + (1 << (j - 1))])
                
        def query_rmq(L_q, R_q):
            if L_q > R_q:
                return 0
            j = log_table[R_q - L_q + 1]
            return max(st[j][L_q], st[j][R_q - (1 << j) + 1])
            
        def eval_seg(idx, L, R, segL, segR):
            if idx <= segL or idx >= segR: return 0
            if type_arr[idx] == 0: return 0
            
            if idx - 1 == segL:
                left_len = max(0, end_idx[idx - 1] - L + 1)
            else:
                left_len = end_idx[idx - 1] - start[idx - 1] + 1
                
            if idx + 1 == segR:
                right_len = max(0, R - start[idx + 1] + 1)
            else:
                right_len = end_idx[idx + 1] - start[idx + 1] + 1
                
            return left_len + right_len

        res = []
        for L, R in queries:
            segL = pos_to_seg[L]
            segR = pos_to_seg[R]
            
            if segR - segL < 2:
                res.append(total_ones)
                continue
                
            max_gain = 0
            max_gain = max(max_gain, eval_seg(segL + 1, L, R, segL, segR))
            max_gain = max(max_gain, eval_seg(segR - 1, L, R, segL, segR))
            
            if segL + 2 <= segR - 2:
                max_gain = max(max_gain, query_rmq(segL + 2, segR - 2))
                
            res.append(total_ones + max_gain)
            
        return res
    
if __name__ == "__main__":
    solution = Solution()
    s = "0100"
    queries = [[0,3],[0,2],[1,3],[2,3]]
    print(solution.maxActiveSectionsAfterTrade(s, queries))  # Output: [4,3,1,1]
    s = "01"
    queries = [[0,1]]
    print(solution.maxActiveSectionsAfterTrade(s, queries))  # Output: [1]
    s = "1000100"
    queries = [[1,5],[0,6],[0,4]]
    print(solution.maxActiveSectionsAfterTrade(s, queries))  # Output: [6,7,2]
    s = "01010"
    queries = [[0,3],[1,4],[1,3]]
    print(solution.maxActiveSectionsAfterTrade(s, queries))  # Output: [4,4,2]