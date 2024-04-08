class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones) 

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 < stone2:
                temp = stone1 - stone2
                heapq.heappush(stones, temp)
        
        if len(stones) == 1:
            return abs(stones[0])
        else:
            return 0




    
        