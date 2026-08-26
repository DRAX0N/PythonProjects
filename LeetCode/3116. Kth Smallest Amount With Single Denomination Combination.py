"""
3116. Kth Smallest Amount With Single Denomination Combination
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array coins representing coins of different denominations and an integer k.

You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.

Return the kth smallest amount that can be made using these coins.

 

Example 1:

Input: coins = [3,6,9], k = 3

Output: 9

Explanation: The given coins can make the following amounts:
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
All of the coins combined produce: 3, 6, 9, 12, 15, etc.

Example 2:

Input: coins = [5,2], k = 7

Output: 12

Explanation: The given coins can make the following amounts:
Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.

 

Constraints:

1 <= coins.length <= 15
1 <= coins[i] <= 25
1 <= k <= 2 * 109
coins contains pairwise distinct integers.
"""
from math import gcd, lcm
from itertools import combinations
from typing import List


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Remove redundant denominations:
        # if a coin is divisible by a smaller coin, it adds no new amounts.
        coins.sort()
        useful_coins = []

        for coin in coins:
            if not any(coin % previous == 0 for previous in useful_coins):
                useful_coins.append(coin)

        coins = useful_coins
        n = len(coins)

        def lcm(a: int, b: int) -> int:
            return a // gcd(a, b) * b

        def count_amounts(x: int) -> int:
            """
            Count distinct positive amounts <= x that are divisible
            by at least one denomination.
            """
            total = 0

            for mask in range(1, 1 << n):
                common_multiple = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        common_multiple = lcm(common_multiple, coins[i])

                        if common_multiple > x:
                            break

                if common_multiple <= x:
                    amount_count = x // common_multiple

                    if bits % 2 == 1:
                        total += amount_count
                    else:
                        total -= amount_count

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            middle = (left + right) // 2

            if count_amounts(middle) >= k:
                right = middle
            else:
                left = middle + 1

        return left

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        filtered_coins: List[int] = []
        for index in range(len(coins)):
            is_valid = True
            for previous_index in range(index):
                if coins[index] % coins[previous_index] == 0:
                    is_valid = False
                    break
            if is_valid:
                filtered_coins.append(coins[index])
        smallest_possible = filtered_coins[0]
        largest_possible = filtered_coins[0] * k
        lcms_to_add: List[int] = []
        lcms_to_substract: List[int] = []
        for r in range(2, 16):
            if r % 2 == 0:
                for combo in combinations(filtered_coins, r):
                    lcms_to_substract.append(lcm(*combo))
            else:
                for combo in combinations(filtered_coins, r):
                    lcms_to_add.append(lcm(*combo))

        def is_possible(num: int) -> bool:
            count_nums = 0
            for coin in filtered_coins:
                count_nums += num // coin
            for lcm_to_add in lcms_to_add:
                count_nums += num // lcm_to_add
            for lcm_to_subtract in lcms_to_substract:
                count_nums -= num // lcm_to_subtract
            return count_nums >= k

        while largest_possible > smallest_possible:
            mid = (smallest_possible + largest_possible) // 2
            if is_possible(mid):
                largest_possible = mid
            else:
                smallest_possible = mid + 1
        return smallest_possible
    
if __name__ == "__main__":
    solution = Solution()
    coins = [3, 6, 9]
    k = 3
    result = solution.findKthSmallest(coins, k)
    print(result)  # Output: 9

    coins = [5, 2]
    k = 7
    result = solution.findKthSmallest(coins, k)
    print(result)  # Output: 12