class MyStack:

    def __init__(self):
        self.dqueue = deque()
        
    def push(self, x: int) -> None:
        self.dqueue.appendleft(x)
        
    def pop(self) -> int:
        return self.dqueue.popleft()
        
    def top(self) -> int:
        if self.dqueue:
            return self.dqueue[0]
        
    def empty(self) -> bool:
        if self.dqueue:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()