class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        sums = set()
        sums.add(0)
        target = sum(nums) /2
        
        for i in range(len(nums)):
            cursums = sums.copy()
            for s in sums:
                cursums.add(s + nums[i])
            sums = cursums
        
        return True if target in sums else False
            
            
            

        