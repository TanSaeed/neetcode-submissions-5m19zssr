class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashy = {}
        self.capacity = capacity

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left


    def remove(self, node):
        prv = node.prev
        nxt = node.next

        prv.next = nxt
        nxt.prev = prv
        node.next = None
        node.prev = None

    def insert(self, node):
        prv = self.right.prev

        prv.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prv

    def get(self, key: int) -> int:
        if key in self.hashy:
            self.remove(self.hashy[key])
            self.insert(self.hashy[key])
            return self.hashy[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashy:
            self.remove(self.hashy[key])
        
        self.hashy[key] = Node(key, value)
        self.insert(self.hashy[key])

        if len(self.hashy) > self.capacity:
            l = self.left.next
            self.remove(l) 
            del self.hashy[l.key]



        
