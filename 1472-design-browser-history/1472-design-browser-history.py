class ListNode:
    def __init__(self, val, prev= None, nxt= None):
        self.val = val
        self.prev = prev
        self.next = nxt

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = ListNode(homepage)   
        self.last = ListNode(0)
        self.cur = self.home
    def visit(self, url: str) -> None:
        newpage = ListNode(url)
        self.cur.next = newpage
        newpage.prev = self.cur
        newpage.next = self.last
        self.last.prev = newpage   
        self.cur = newpage
        
    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0 :
            self.cur = self.cur.prev
            steps -=1
        return self.cur.val
            
    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next and self.cur.next!=self.last:
            self.cur = self.cur.next
            steps -=1   
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)