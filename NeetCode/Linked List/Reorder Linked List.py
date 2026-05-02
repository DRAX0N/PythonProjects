"""
Reorder Linked List
Medium
Topics
Company Tags
Hints
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]

Output: [2,8,4,6]
Example 2:

Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]
Constraints:

1 <= Length of the list <= 1000.
1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"{self.val} -> {self.next}" if self.next else f"{self.val}"

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def last_value(head, target = None):
            while head:
                if head.next == target:
                    head.next = None
                    return head
                head = head.next
        
        head_values = []
        while head:
            head_values.append(head.val)
            head = head.next
        print(head_values)
        ans = ListNode(head_values[0])
        head_values.pop(0)

        i = 0
        while head_values:
            
            if i%2 == 1:
                ans = ListNode(ans, ListNode(head_values[0]))
                head_values.pop(0)
            else:
                ans = ListNode(ans, ListNode(head_values[-1]))
                head_values.pop(-1)

            i += 1
        return ans
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return head

if __name__ == "__main__":

    head = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))
    print(Solution().reorderList(head))# Output: [2,8,4,6]
    
    print("=================================================")
    head = ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10)))))
    print(Solution().reorderList(head))# Output: [2,10,4,8,6]