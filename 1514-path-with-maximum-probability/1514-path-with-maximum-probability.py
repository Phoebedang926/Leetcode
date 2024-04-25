class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            adj[a].append([b, succProb[i]])
            adj[b].append([a, succProb[i]])
        
        maxsucess = {}
        maxheap = [[-1,start_node]]
        visit = set()
        while maxheap:
            p1,n1 = heapq.heappop(maxheap)
            visit.add(n1)
            if n1 == end_node: return - p1
            if n1 in maxsucess:
                continue
            maxsucess[n1] = p1
            
            for n2,p2 in adj[n1]:
                if n2 not in maxsucess and n2 not in visit:
                    heapq.heappush(maxheap, [p1*p2, n2])
                    
        return 0
        

        