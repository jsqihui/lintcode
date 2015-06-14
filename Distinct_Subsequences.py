class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here
        dp = [[0 for _ in range(len(T)+1)] for _ in range(len(S)+1)]
        
        for i in range(len(S)+1):
            dp[i][0] = 1
        
        for i in range(1, len(S)+1):
            for j in range(1, len(T)+1):
                dp[i][j] = dp[i-1][j]
                if T[j-1] == S[i-1]:
                    dp[i][j] += dp[i-1][j-1]
        
        return dp[len(S)][len(T)]

