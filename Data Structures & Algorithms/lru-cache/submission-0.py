class ListNode:
    def __init__(self,key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.front = ListNode(None, None)
        self.back = ListNode(None, None)

        self.front.next = self.back
        self.back.prev = self.front        

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
            
    
        self.remove(self.hashmap[key])
        self.add(self.hashmap[key])

        return self.hashmap[key].val
    
    def remove(self, node: ListNode):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def add(self, node: ListNode):
        node.next = self.front.next
        node.prev = self.front
        self.front.next.prev = node
        self.front.next = node


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        node = ListNode(key, value)
        self.hashmap[key] = node
        self.add(node)

        if len(self.hashmap) > self.capacity:
            lru = self.back.prev
            self.remove(lru)
            del self.hashmap[lru.key]   # this is why nodes store the key