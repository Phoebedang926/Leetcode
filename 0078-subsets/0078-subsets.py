class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for i in nums:
            for j in range(len(subset)):
                subset.append(subset[j].copy())                
                subset[j].append(i)
        return subset
                
            
