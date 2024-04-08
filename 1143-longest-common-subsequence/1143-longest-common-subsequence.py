class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        dp = [[0 for c in range(len2+1)] for r in range(len1+1)]

        for r in range(len1-1, -1, -1):
            for c in range(len2-1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else: 
                    dp[r][c] = max(dp[r][c+1], dp[r+1][c])
        
        return dp[0][0]
            
        