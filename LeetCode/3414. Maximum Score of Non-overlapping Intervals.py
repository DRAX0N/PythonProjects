"""
3414. Maximum Score of Non-overlapping Intervals
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.

Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

 

Example 1:

Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

Output: [2,3]

Explanation:

You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

Example 2:

Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

Output: [1,3,5,6]

Explanation:

You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

 

Constraints:

1 <= intevals.length <= 5 * 104
intervals[i].length == 3
intervals[i] = [li, ri, weighti]
1 <= li <= ri <= 109
1 <= weighti <= 109
"""
from typing import List
import bisect

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        if n == 0:
            return []
        
        # Dodajemy oryginalne indeksy do przedziałów
        augmented = [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)]
        
        # Sortujemy według końca przedziału
        augmented.sort(key=lambda x: x[1])
        
        # Przygotowujemy listę końców dla wyszukiwania binarnego
        ends = [augmented[i][1] for i in range(n)]
        
        NEG_INF = float('-inf')
        
        # dp[k][i] = (max_weight, list_of_indices) dla k przedziałów spośród pierwszych i
        dp = [[(NEG_INF, []) for _ in range(n + 1)] for _ in range(5)]
        
        # Inicjalizacja: 0 przedziałów daje wagę 0
        for i in range(n + 1):
            dp[0][i] = (0, [])
        
        for i in range(1, n + 1):
            left, right, weight, orig_idx = augmented[i - 1]
            
            # Znajdź liczbę przedziałów, które kończą się przed 'left'
            pos = bisect.bisect_left(ends, left)
            prev_idx = pos
            
            for k in range(1, 5):
                # Opcja 1: nie bierzemy bieżącego przedziału
                best_weight, best_indices = dp[k][i - 1]
                
                # Opcja 2: bierzemy bieżący przedział
                if prev_idx >= 0 and dp[k - 1][prev_idx][0] != NEG_INF:
                    prev_weight, prev_indices = dp[k - 1][prev_idx]
                    new_weight = prev_weight + weight
                    new_indices = prev_indices + [orig_idx]
                    
                    # Sortujemy indeksy dla poprawnego porównania leksykograficznego
                    new_indices_sorted = sorted(new_indices)
                    best_indices_sorted = sorted(best_indices)
                    
                    if new_weight > best_weight:
                        best_weight, best_indices = new_weight, new_indices
                    elif new_weight == best_weight and new_indices_sorted < best_indices_sorted:
                        best_indices = new_indices
                
                dp[k][i] = (best_weight, best_indices)
        
        # Znajdź najlepsze rozwiązanie spośród 0, 1, 2, 3, 4 przedziałów
        best_result = (NEG_INF, [])
        for k in range(0, 5):
            weight, indices = dp[k][n]
            indices_sorted = sorted(indices)
            best_indices_sorted = sorted(best_result[1])
            
            if weight > best_result[0]:
                best_result = (weight, indices)
            elif weight == best_result[0] and indices_sorted < best_indices_sorted:
                best_result = (weight, indices)
        
        return sorted(best_result[1])


if __name__ == "__main__":
    solution = Solution()
    intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]
    print(solution.maximumWeight(intervals))  # Output: [2,3]

    intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]
    print(solution.maximumWeight(intervals))  # Output: [1,3,5,6]

    intervals = [[4,4,1],[2,5,3],[2,3,2]]
    print(solution.maximumWeight(intervals))  # Output: [0,2]