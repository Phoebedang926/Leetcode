# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         cache = {}
#         def dp(i,j):
#             if j == len(t):
#                 return 1
#             if i == len(s):
#                 return 0
#             if (i,j) in cache:
#                 return cache[(i,j)]
            
#             if s[i] == t[j]:
#                 cache[(i,j)] = dp(i+1,j+1) + dp(i+1,j)
#             else:
#                 cache[(i,j)] = dp(i+1,j)
#             return cache[(i,j)]
#         return dp(0,0)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        dp = [0] * (M+1) 
        dp[M] = 1
        for n in range(N-1,-1, -1):
            curdp = [0] * (M+1)
            curdp[M] = 1
            for m in range(M-1,-1,-1):
                if s[n] == t[m]:
                    curdp[m] = dp[m+1] + dp[m]
                else:
                    curdp[m] = dp[m]
            dp = curdp
        return dp[0]
