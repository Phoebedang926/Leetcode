class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in remain:
                return [i,remain[diff]]
            remain[num] = i
        
            
