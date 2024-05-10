class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rs = s[::-1]
        dp = [0]*(len(s)+1)
        
        for i in range(len(s)-1, -1, -1):
            curdp = [0]*(len(s)+1)
            for j in range(len(rs)-1, -1, -1):                
                if s[i] == rs[j]:
                    curdp[j] = 1 + dp[j+1]
                else:
                    curdp[j] = max(dp[j], curdp[j+1])
            dp = curdp
        return dp[0]
                    

                