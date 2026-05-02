"""
Add Two Numbers
Medium
Topics
Company Tags
Hints
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:



Input: l1 = [1,2,3], l2 = [4,5,6]

Output: [5,7,9]

Explanation: 321 + 654 = 975.
Example 2:

Input: l1 = [9], l2 = [9]

Output: [8,1]
Constraints:

1 <= l1.length, l2.length <= 100.
0 <= Node.val <= 9
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"{self.val} -> {self.next}" if self.next else f"{self.val}"
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #carry = 0
        #head = ListNode(0, None)
        #current = head
        #
        #res = 0
#
        #while l1 and l2:
        #    temp = ListNode(0, None)
        #    res = l1.val + l2.val + carry
        #    if res > 9:
        #        res -= 10
        #        carry = 1
        #    else:
        #        carry = 0
        #    temp.val = res
        #    current = temp
        #    l1 = l1.next
        #    l2 = l2.next
        #    current = current.next
#
        #return current
        def list_length(head, target = None):
            i = 0
            while head:
                if head.next == target:
                    head.next = None
                    i+=1
                    return head
                head = head.next

        l1_len = list_length(l1)
        l2_len = list_length(l2)

        oldToCopy = []
        carry = 0
        
        while l1 or l2 or carry != 0:

            if l1 and l2:
                res = l1.val + l2.val + carry
            elif l1:
                res = l1.val + carry
            elif l2:
                res = l2.val + carry
            else:
                res = carry

            if res > 9:
                res -= 10
                carry = 1
            else:
                carry = 0

            copy = ListNode(res)
            oldToCopy.append(copy)

            if l1 and l2:
                l1 = l1.next
                l2 = l2.next
            elif l1:
                l1 = l1.next
            elif l2:
                l2 = l2.next

        cur = oldToCopy[0]
        for element in oldToCopy[1:]:
            cur.next = element
            cur = cur.next
        
        return oldToCopy[0]


if __name__ == "__main__":

    l1 = ListNode(1, ListNode(2, ListNode(3)))
    l2 = ListNode(4, ListNode(5, ListNode(6)))
    print(Solution().addTwoNumbers(l1, l2)) # [5,7,9]

    l1 = ListNode(9)
    l2 = ListNode(9)
    print(Solution().addTwoNumbers(l1, l2)) # [8,1]