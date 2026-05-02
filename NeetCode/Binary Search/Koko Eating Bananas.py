"""
Koko Eating Bananas
Medium
Topics
Company Tags
Hints
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:

Input: piles = [1,4,3,2], h = 9

Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

Example 2:

Input: piles = [25,10,23,4], h = 4

Output: 25
Constraints:

1 <= piles.length <= 1,000
piles.length <= h <= 1,000,000
1 <= piles[i] <= 1,000,000,000
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def banana_counter(k, piles):
            hours_to_eat = 0
            for banana in piles:
                if banana % k == 0:
                    hours_to_eat += banana // k
                else:
                    hours_to_eat += banana // k + 1
            return hours_to_eat
        min_v = 1
        max_v = max(piles)
        k = 1
        res = 0
        while min_v<=max_v:
            k=(min_v+max_v)//2
            if banana_counter(k, piles)>h: # and banana_counter(k+1, piles)!=banana_counter(k, piles):
                min_v = k + 1
            else:
                res = k
                max_v = k - 1
            
        return res
                



if __name__ == '__main__':
    piles = [1,4,3,2]
    h = 9                   # output 2

    #piles = [25,10,23,4] 
    #h = 4                   # output 25

    #piles=[1,1,1,999999999]
    #h=10                        #142857143

    new = Solution()
    print(new.minEatingSpeed(piles, h)) 