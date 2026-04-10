class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key: pointer to node

        self.left = Node(0, 0) # Least Used
        self.right = Node(0, 0) # Recently Used

        self.left.next = self.right
        self.right.prev = self.left


    def remove(self, node): # remove node from list
        prev, nxt = node.prev, node.next
        
        prev.next = nxt
        nxt.prev = prev

        node.next = None
        node.prev = None


    def insert(self, node): # insert node at right
        prev = self.right.prev

        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key]) # most recently used so we want to move it to the right
            #todo: update most recent
            return self.cache[key].val
        return -1

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap: # cap met, remove from left linked list, delete key:pointer
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        
