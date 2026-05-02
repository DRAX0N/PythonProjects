"""
Two Integer Sum II
Medium
Topics
Company Tags
Hints
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O
(
1
)
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Constraints:

2 <= numbers.length <= 1000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, number in enumerate(numbers):
            if (target-number) in numbers[index+1::]:
                index2 = numbers[index+1::].index((target-number))
                return [index+1, index2+len(numbers[0:index+1:])+1]
        return []
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1

        while l < r:
            compliment = target - numbers[l] - numbers[r]
            if compliment > 0:
                l +=1
            elif compliment < 0:
                r -=1
            else:
                return [l+1, r+1]

        return []
if __name__ == '__main__':
    numbers = [2,3,4]
    target = 6

    new = Solution()
    print(new.twoSum(numbers, target))