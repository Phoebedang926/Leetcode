class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            nextperms = []
            for p in perms:
                for i in range(len(p)+1):
                    pcopy = p.copy()
                    pcopy.insert(i,n)
                    nextperms.append(pcopy)
                    
            perms = nextperms
        my_set = set(tuple(sublist) for sublist in perms)
        
        return my_set
        