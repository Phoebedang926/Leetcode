class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i,n in enumerate(nums):
            diff = target - n
            if n in diffs:
                return [diffs[n], i]
            else:
                diffs[diff] = i
        
            
            
            

            
