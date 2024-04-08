class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            dis = x**2 + y**2
            minheap.append([dis,x,y])
        heapq.heapify(minheap)
        
        res = []
        while k > 0:
            dis,x,y = heapq.heappop(minheap)
            res.append([x,y])
            k -=1
        return res



        # dis = {}
        # for i in range(len(points)):
        #     dis[i] = points[i][0]**2 + points[i][1]**2  # Corrected exponentiation operator

        # sorted_dict = sorted(dis.items(), key=lambda x: x[1])
        # keys_subset = [key for key, _ in sorted_dict[:k]]  # Extract keys from sorted dictionary

        # result = [points[key] for key in keys_subset]  # Extract corresponding points
        # return result
