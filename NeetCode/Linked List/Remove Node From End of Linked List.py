"""
Remove Node From End of Linked List
Medium
Topics
Company Tags
Hints
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
Example 2:

Input: head = [5], n = 1

Output: []
Example 3:

Input: head = [1,2], n = 2

Output: [2]
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}" if self.next else f"{self.val}"

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def last_value(head, target = None):
            counter = 0
            while head:
                counter += 1
                if head.next == target:
                    head.next = None
                    return counter
                head = head.next

        len_head = last_value(head)

        index = len_head - n
        print("index = " + str(index))
        #print(len_head)
        current = head
        next  = head.next
        #current = head
        i = 0
        if index == 0:
            return head.next
        while head and head.next:
            if i == index - 1:
                current.next = next.next
                break
            current = current.next
            next = next.next
            i += 1

        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
    
    
if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(solution.removeNthFromEnd(head, 2)) # [1,2,4]
    head = ListNode(5)
    #print(solution.removeNthFromEnd(head, 1)) # []
    head = ListNode(1, ListNode(2))
    #print(solution.removeNthFromEnd(head, 2)) # [2]
    