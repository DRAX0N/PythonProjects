"""
Docstring for NeetCode.sort_ascending
Sort Ascending
In Python, you can sort a list of elements by calling .sort() on the list.

elements = [5, 3, 6, 2, 1]

elements.sort()

print(elements) # [1, 2, 3, 5, 6]
By default, the .sort() method sorts the elements in ascending order in-place. The return value of the .sort() method is None.

This method also works for a list of strings.

elements = ["grape", "apple", "banana", "orange"]

elements.sort()

print(elements) # ['apple', 'banana', 'grape', 'orange']
By default, strings are sorted in lexicographical order.

Challenge
Implement the following functions:

sort_words(words: List[str]) -> List[str] - This function accepts a list of words and returns the list of words sorted in ascending order.
sort_numbers(numbers: List[int]) -> List[int] - This function accepts a list of numbers and returns the list of numbers sorted in ascending order.
sort_decimals(numbers: List[float]) -> List[float] - This function accepts a list of decimal numbers and returns the list of decimal numbers sorted in ascending order.
Time and Space Complexity
The time complexity of the .sort() method is 
O
(
n
l
o
g
n
)
O(nlogn), where n is the number of elements in the list.
The space complexity is 
O
(
n
)
O(n), where n is the number of elements in the list.
Note: Python uses the Timsort algorithm for sorting lists. Timsort is a hybrid sorting algorithm derived from merge sort and insertion sort. To learn more about sorting, check out the Data Structures and Algorithms for Beginners course.
"""

from typing import List


def sort_words(words: List[str]) -> List[str]:
    pass

def sort_numbers(numbers: List[int]) -> List[int]:
    pass

def sort_decimals(numbers: List[float]) -> List[float]:
    pass



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))