class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, curset = [], []        
        
        def dfs(i):
            if i >= len(nums):
                subsets.append(curset.copy())
                return
            
            # add i
            curset.append(nums[i])
            dfs(i+1)
            
            #not add i
            curset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)
            
        dfs(0)   
        return subsets
        