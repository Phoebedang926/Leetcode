class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pres = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pres[crs].append(pre)
        
        res = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit: return True
            cycle.add(crs)

            for pre in pres[crs]:
                if not dfs(pre): return False
            res.append(crs)
            cycle.remove(crs)
            visit.add(crs)
            return True

        for i in range(numCourses):
            if not dfs(i): return []
        return res




        