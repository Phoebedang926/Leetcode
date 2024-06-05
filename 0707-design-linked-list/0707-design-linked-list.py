class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left       
        

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if index == 0 and cur and cur != self.right:
            return cur.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        newHead = ListNode(val)
        head = self.left.next
        
        self.left.next = newHead
        newHead.next = head
        newHead.prev = self.left
        head.prev = newHead
        

    def addAtTail(self, val: int) -> None:
        newTail = ListNode(val)
        tail = self.right.prev
        
        self.right.prev = newTail
        newTail.prev = tail
        newTail.next = self.right
        tail.next = newTail
             

    def addAtIndex(self, index: int, val: int) -> None:        
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if index == 0 and cur:
            newNode = ListNode(val)
            prevNode = cur.prev
        
            cur.prev = newNode
            newNode.prev = prevNode
            newNode.next = cur
            prevNode.next = newNode



    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if index == 0 and cur and cur != self.right:
            prevNode, nextNode = cur.prev, cur.next
            prevNode.next = nextNode
            nextNode.prev = prevNode



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)