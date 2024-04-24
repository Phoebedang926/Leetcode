class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         perms = [[]]
#         for n in nums:
#             nextperms = []
#             for p in perms:
#                 for i in range(len(p)+1):
#                     pcopy = p.copy()
#                     pcopy.insert(i,n)
#                     nextperms.append(pcopy)
                    
#             perms = nextperms
#         my_set = set(tuple(sublist) for sublist in perms)
        
#         return my_set

        #optimize
        res = []
        perm = []
        count = {n: 0 for n in nums}
        for n in nums:
            count[n] +=1
        
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -=1
                    
                    dfs()
                    perm.pop()
                    count[n] +=1
        dfs()
        return res