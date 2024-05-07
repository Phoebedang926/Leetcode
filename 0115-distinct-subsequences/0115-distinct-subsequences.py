class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dp(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            
            if s[i] == t[j]:
                cache[(i,j)] = dp(i+1,j+1) + dp(i+1,j)
            else:
                cache[(i,j)] = dp(i+1,j)
            return cache[(i,j)]
        return dp(0,0)
# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         N, M = len(s), len(t)
#         dp = [0] * (N+1)
#         dp[0] = 1
#         for m in range(M):
#             curdp = [0] * (N+1)
#             for n in range(N):
#                 if s[n] == t[m]:
#                     curdp[n+1] += dp[n]
#                 curdp[n+1] += curdp[n]
#             dp = curdp
#         return dp[N]
        