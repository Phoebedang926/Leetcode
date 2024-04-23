class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if len(subset) == k:
                res.append(subset.copy())
                return
            if i > n: return
            
#             subset.append(i)
#             dfs(i+1)
            
#             subset.pop()
#             dfs(i+1)
            
        # optimize
            for j in range(i,n+1):
                subset.append(j)
                dfs(j+1)
                subset.pop()
        dfs(1)
        return res
                
            
        