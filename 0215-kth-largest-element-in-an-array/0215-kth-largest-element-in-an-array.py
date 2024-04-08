class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        while k >0:
            if k ==1:
                return - heapq.heappop(nums)
            heapq.heappop(nums)
            k -= 1

        