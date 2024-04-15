class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
#Path Compression
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False # there is a cycle

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailtoacc = {}
        
        for i,acc in enumerate(accounts):
            for e in acc[1:]:                             
                if e in emailtoacc:                        
                    uf.union(i, emailtoacc[e])
                else:
                    emailtoacc[e] = i  
        
        emailgroup = defaultdict(list)
        for e,i in emailtoacc.items():
            leader = uf.find(i)
            emailgroup[leader].append(e)
        res = []     
        for i, emails in emailgroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailgroup[i]))
        return res                                 