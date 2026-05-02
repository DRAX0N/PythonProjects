"""
Merge Two Sorted Linked Lists
Solved 
Easy
Topics
Company Tags
Hints
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:



Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2]
Example 3:

Input: list1 = [], list2 = []

Output: []
Constraints:

0 <= The length of the each list <= 100.
-100 <= Node.val <= 100

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        newHead = ListNode()

        if list1 and list2 and list1.val <= list2.val:
            newHead = list1
            newHead.next = self.mergeTwoLists(list1.next, list2)
        elif list1 and list2 and list1.val > list2.val:
            newHead = list2
            newHead.next = self.mergeTwoLists(list1, list2.next)
        elif list1:
            newHead = list1
            newHead.next = self.mergeTwoLists(list1.next, list2)
        elif list2:
            newHead = list2
            newHead.next = self.mergeTwoLists(list1, list2.next)

        
        return newHead
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2
        #if l1:
        #    node.next = list1
        #elif l2:
        #    node.next = list2

        return dummy.next
        
if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(5, ListNode(6))))
    print(Solution().mergeTwoLists(list1, list2)) # [1,1,2,3,4,5]

    list1 = ListNode()
    list2 = ListNode(1, ListNode(2))
    print(Solution().mergeTwoLists(list1, list2)) # [1,2]

    list1 = ListNode()
    list2 = ListNode()
    print(Solution().mergeTwoLists(list1, list2)) # []