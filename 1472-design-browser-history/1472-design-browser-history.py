class ListNode:
    def __init__(self, val, prev= None, nxt= None):
        self.val = val
        self.next = nxt
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)      

    def visit(self, url: str) -> None:
        newNode = ListNode(url,self.cur)
        self.cur.next = newNode
        self.cur = self.cur.next
        
    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.prev:
            self.cur = self.cur.prev
            steps -=1               
        return self.cur.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next:
            self.cur = self.cur.next
            steps -=1              
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)