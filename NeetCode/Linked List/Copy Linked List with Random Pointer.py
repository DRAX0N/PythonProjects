"""
Copy Linked List with Random Pointer
Medium
Topics
Company Tags
Hints
You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

Example 1:



Input: head = [[3,null],[7,3],[4,0],[5,1]]

Output: [[3,null],[7,3],[4,0],[5,1]]
Example 2:



Input: head = [[1,null],[2,2],[3,2]]

Output: [[1,null],[2,2],[3,2]]
Constraints:

0 <= n <= 100
-100 <= Node.val <= 100
random is null or is pointing to some node in the linked list.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        l1 = head
        while l1 is not None:
            l2 = Node(l1.val)
            l2.next = l1.next
            l1.next = l2
            l1 = l2.next

        newHead = head.next

        l1 = head
        while l1 is not None:
            if l1.random is not None:
                l1.next.random = l1.random.next
            l1 = l1.next.next

        l1 = head
        while l1 is not None:
            l2 = l1.next
            l1.next = l2.next
            if l2.next is not None:
                l2.next = l2.next.next
            l1 = l1.next

        return newHead
    
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    
    def __str__(self):
        return f"{self.val} -> {self.next}" if self.next else f"{self.val}"


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def hashmap_from_head(nodes):
            hashmap = {}
            i = 0
            while nodes:
                i += 1
                if nodes.random != None:
                    hashmap[i] = [nodes.val, nodes.random.val]
                else:
                    hashmap[i] = [nodes.val, None]
                nodes = nodes.next
            return hashmap
            
        if not head:
            return None
        
        hashmap = hashmap_from_head(head)
        print(hashmap)
        front = None
        tail = None

        for v in hashmap.keys():
            new_node = Node(hashmap[v][0])
            new_node.random = hashmap[v][1]
            if front is None:
                front = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

        print(front)
        

        #for key in hashmap.keys():
        #    if key == 1:
        #        answer = dummy = Node(hashmap[key][0], None, None)
        #    else:
        #        temp = dummy.next
        #        temp = Node(hashmap[key][0], None, None)
        #        temp = temp.next
        #print(temp)
#
        #print(hashmap)

        #dummy = Node()
#
        #while head and head.next:
        #    dummy = Node(head.val, head.random)
        #    head = head.next
        #    
        #return dummy
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
    
if __name__ == "__main__":
    head = Node(3, None, None)
    head.next = Node(7, None, None)
    head.next.next = Node(4, None, None)
    head.next.next.next = Node(5, None, None)

    head.random = None
    head.next.random = head.next.next.next
    head.next.next.random = head
    head.next.next.next.random = head.next

    solution = Solution()
    print(solution.copyRandomList(head)) # [[3,null],[7,3],[4,0],[5,1]]

    head = Node(1, None, None)
    head.next = Node(2, None, None)
    head.next.next = Node(3, None, None)

    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next

    #print(solution.copyRandomList(head)) # [[1,null],[2,2],[3,2]]