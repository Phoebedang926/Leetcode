class Solution:
    def fib(self, n: int) -> int:
        n_1, n_2 = 1,0
        for i in range (n-1):
            n = n_1 + n_2
            n_2 = n_1
            n_1 = n
        return n

            
        
        
        # if n <= 1:
        #     return n
        # else:
        #     return self.fib(n-1) + self.fib(n-2)
