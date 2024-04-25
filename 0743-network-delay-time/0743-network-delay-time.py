class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        
        for u,v,w in times:
            adj[u].append([v,w])
            
        shortest = {}
        minheap = [[0,k]]
        while minheap:
            w1,n1 = heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1]=w1
            if len(shortest) == n:
                return w1
            
            for n2,w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap, [w1+w2, n2])
        
        return -1
        
        