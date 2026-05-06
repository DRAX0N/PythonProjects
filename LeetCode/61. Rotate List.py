"""
61. Rotate List
Medium
Topics
premium lock icon
Companies
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       if not head:
           return None

       tail = head
       length = 1
       while tail.next:
           tail = tail.next
           length += 1

       # Connect the tail to the head to make it a circular list
       tail.next = head

       # Find the new tail: (length - k % length - 1)th node
       # and the new head: (length - k % length)th node
       k = k % length
       new_tail = head
       for _ in range(length - k - 1):
           new_tail = new_tail.next

       new_head = new_tail.next

       # Break the circle
       new_tail.next = None

       return new_head
    
class Solution:
    def rotateRight(self, head,k):
        if head is None or head.next is None:
            return head
        n=1
        last=head
        while(last.next!=None):
            n+=1
            last=last.next
        k=k%n
        if k==0:
            return head   
        t=head
        count=1
        while t is  not None:
            if count== (n-k):
                break
            count+=1
            t=t.next
        new_head=t.next
        t.next=None
        last.next=head   
        return new_head  
    
if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    new_head = s.rotateRight(head, k)
    # Print the rotated list
    while new_head:
        print(new_head.val, end=" ")  # Output: 4 5 1 2 3
        new_head = new_head.next

    print()  # for a new line

    head = ListNode(0, ListNode(1, ListNode(2)))
    k = 4
    new_head = s.rotateRight(head, k)
    # Print the rotated list
    while new_head:
        print(new_head.val, end=" ")  # Output: 2 0 1
        new_head = new_head.next



