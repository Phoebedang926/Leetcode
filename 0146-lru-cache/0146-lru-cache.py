class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self,node):
        prenode, nxtnode = node.prev, node.next
        prenode.next, nxtnode.prev = nxtnode, prenode
        
    def insert(self,node):
        prenode = self.right.prev
        prenode.next = node
        node.prev, node.next = prenode, self.right
        self.right.prev = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newnode = ListNode(key, value)
        self.cache[key] = newnode
        self.insert(self.cache[key])        
        if len(self.cache) > self.cap:
            LRU = self.left.next
            del self.cache[LRU.key]
            self.remove(LRU)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)