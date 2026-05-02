"""
Merge K Sorted Linked Lists
Hard
Topics
Company Tags
Hints
You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.

Example 1:

Input: lists = [[1,2,4],[1,3,5],[3,6]]

Output: [1,1,2,3,3,4,5,6]
Example 2:

Input: lists = []

Output: []
Example 3:

Input: lists = [[]]

Output: []
Constraints:

0 <= lists.length <= 1000
0 <= lists[i].length <= 100
-1000 <= lists[i][j] <= 1000

"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while True:
            min_node = None
            min_index = -1
            for i in range(len(lists)):
                if lists[i] is not None:
                    if min_node is None or lists[i].val < min_node.val:
                        min_node = lists[i]
                        min_index = i
            if min_node is None:
                break
            tail.next = min_node
            tail = tail.next
            lists[min_index] = lists[min_index].next
        return dummy.next







if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(5)))
    l3 = ListNode(3, ListNode(6))
    print(s.mergeKLists([l1, l2, l3])) # [1,1,2,3,3,4,5,6]

    l1 = ListNode()
    l2 = ListNode(1, ListNode(2))
    print(s.mergeKLists([l1, l2])) # [1,2]

    l1 = ListNode()
    l2 = ListNode()
    print(s.mergeKLists([l1, l2])) # []