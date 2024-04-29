class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)
            
        premap = {}
        visit = set()
        def dfs(crs):
            if crs not in premap:
                premap[crs] = set()
                for pre in adj[crs]:
                    premap[crs] |= dfs(pre)
                
            premap[crs].add(crs)    
            return premap[crs]
        

        
        for i in range(numCourses):
            dfs(i)
        
        res = []
        for pre, crs in queries:
            res.append(pre in premap[crs])
        return res
        
        