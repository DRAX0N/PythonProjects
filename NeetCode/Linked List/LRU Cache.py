"""
LRU Cache
Medium
Topics
Company Tags
Hints
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in 
O
(
1
)
O(1) average time complexity.

Example 1:

Input:
["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

Output:
[null, null, 10, null, null, 20, -1]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20 
lRUCache.get(1);      // return -1 (not found)
Constraints:

1 <= capacity <= 100
0 <= key <= 1000
0 <= value <= 1000
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = {}
        self.keys = []

    def get(self, key: int) -> int:
        if key in self.keys:
            self.keys.pop(self.keys.index(key))
            self.keys.append(key)
            return self.dictionary[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None: 
        self.dictionary[key] = value
        if key in self.keys:
            self.keys.pop(self.keys.index(key))
        if len(self.keys) == self.capacity:
            key_to_remove = self.keys.pop(0)
            self.dictionary.pop(key_to_remove)
        self.keys.append(key)

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node_to_head(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    
    def _remove_node(self, node: Node):
        node_next = node.next
        node_prev = node.prev
        node_prev.next = node_next
        node_next.prev = node_prev


    def _move_node_to_head(self, node: Node):
        self._remove_node(node)
        self._add_node_to_head(node)
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self._move_node_to_head(node)
            return node.value


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            new_node = Node(key, value)
            self._add_node_to_head(new_node)
            self.cache[key] = new_node
            if len(self.cache) > self.capacity:
                removed_node = self.tail.prev
                self._remove_node(removed_node)
                del self.cache[removed_node.key]
        else:
            existing_node = self.cache[key]
            existing_node.value = value
            self._move_node_to_head(existing_node)

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 10)  # cache: {1=10}
    print(lRUCache.get(1))      # return 10
    lRUCache.put(2, 20)  # cache: {1=10, 2=20}
    lRUCache.put(3, 30)  # cache: {2=20, 3=30}, key=1 was evicted
    print(lRUCache.get(2))      # returns 20 
    print(lRUCache.get(1))      # return -1 (not found)