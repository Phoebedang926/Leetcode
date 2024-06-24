class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev  = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index >0:
            cur  = cur.next
            index -=1
        if index == 0 and cur and cur != self.tail: 
            return cur.val 
        return -1

    def addAtHead(self, val: int) -> None:
        nxtnode = self.head.next
        newnode = ListNode(val)
        self.head.next = newnode
        newnode.prev = self.head
        newnode.next = nxtnode
        nxtnode.prev = newnode

    def addAtTail(self, val: int) -> None:
        prevnode = self.tail.prev
        newnode = ListNode(val)
        self.tail.prev = newnode
        newnode.next = self.tail
        newnode.prev = prevnode
        prevnode.next = newnode

    def addAtIndex(self, index: int, val: int) -> None:  
        cur = self.head.next
        while cur and index >0:
            cur  = cur.next
            index -=1
        if index  == 0 and cur: 
            newnode = ListNode(val)
            prevnode = cur.prev
            cur.prev = newnode
            newnode.next = cur
            newnode.prev = prevnode
            prevnode.next = newnode

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while cur and index > 0:
            cur  = cur.next
            index -=1
        if index == 0 and cur and cur != self.tail : 
            prev = cur.prev
            nxt = cur.next
            prev.next = nxt
            nxt.prev = prev



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)