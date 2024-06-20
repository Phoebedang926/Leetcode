class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x,y in points:
            dis = sqrt(x**2 + y**2)
            minheap.append([dis,x,y])
        heapq.heapify(minheap)
        res = []
        for i in range(k):
            dis,x,y = heapq.heappop(minheap)
            res.append([x,y])
        return res
            
