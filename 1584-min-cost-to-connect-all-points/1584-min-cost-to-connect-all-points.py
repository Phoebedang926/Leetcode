class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        n = len(points)
        for i in range(n):
            adj[i] = []
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([j,dist])
                adj[j].append([i,dist])
        
        minheap =[[0,0]]        
        res = 0
        visit = set()
        
        while len(visit) < n:
            d1,n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue           
            res += d1
            visit.add(n1)
            for n2,d2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, [d2,n2])
        return res