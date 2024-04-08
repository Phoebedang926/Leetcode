class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []


        def dfs(i, cursum):
            if cursum == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or cursum > target:                
                return
                     
           # include
            subset.append(candidates[i])          
            dfs(i, cursum + candidates[i])

            # not include
            subset.pop()
            dfs(i+1, cursum)
        
        dfs(0,0)
        return res
        