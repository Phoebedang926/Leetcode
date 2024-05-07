class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        dp = [0] * (M+1)
        for n in range(N):
            curdp = [0] * (M+1)
            for m in range(M):
                if text1[n] == text2[m]:
                    curdp[m+1] = 1 + dp[m]
                else:
                    curdp[m+1] = max(dp[m+1], curdp[m])
            dp = curdp
        return dp[M]
    
        