class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = {}
        for i in range(len(nums)):
            remain[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in remain and i!=remain[nums[i]]:
                return[i,remain[nums[i]]]
        
            
