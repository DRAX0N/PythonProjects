"""
2130. Maximum Twin Sum of a Linked List
Medium
Topics
premium lock icon
Companies
Hint
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"{self.val} -> {self.next}" if self.next else f"{self.val}"
    
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = []
        while head != None:
            temp.append(head.val)
            head = head.next
        temp_len = len(temp)
        max_value = 0
        for i in range(temp_len//2):
            max_value = max(max_value, (temp[i]+temp[temp_len-1-i]))
        return max_value
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return None
        if not head.next.next:
            return head.val + head.next.val
        
        best = 0
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        previ = None
        while slow:
            temp = slow.next
            slow.next = previ
            previ = slow
            slow = temp
        start = head

        while previ:
            result = start.val + previ.val
            if result > best:
                best = result
            start = start.next
            previ = previ.next
        return best
            

if __name__ == "__main__":

    head = ListNode(5)
    head.next = ListNode(4)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    #head.next.next.next.next = head.next
    print(Solution().pairSum(head)) #6

    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    #head.next.next.next.next = head.next
    print(Solution().pairSum(head)) #7

    head = ListNode(1)
    head.next = ListNode(1000)
    #head.next.next.next.next = head.next
    print(Solution().pairSum(head)) #10001