class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for i in range(n + 1)] for i in range(m + 1)]

        for s in strs:
            zeros, ones = s.count('0'), s.count('1')
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i-zeros][j-ones] + 1, dp[i][j])

        return dp[m][n]
        # dp = defaultdict(int)

        # for s in strs:
        #     mcount, ncount = s.count("0"), s.count("1")
        #     for mnum in range(m, mcount - 1, -1):  # Reverse loop to avoid overwriting
        #         for nnum in range(n, ncount - 1, -1):  # Reverse loop to avoid overwriting
        #             dp[(mnum, nnum)] = max(1 + dp[(mnum - mcount, nnum - ncount)], dp[(mnum, nnum)])

        # return dp[(m, n)]
        