class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            newstone = -abs(stone1 -stone2)
            if newstone !=0:
                heapq.heappush(stones,newstone)
        if stones:
            return -stones[0]
        else:
            return 0





    
        