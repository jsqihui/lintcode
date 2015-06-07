class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        # write your code here
        
#        dp = [[0 for _ in range(m+1)] for _ in range(len(A)+1)]
#        
#        for i in range(1, len(A)+1):
#            for j in range(1, m+1):
#                dp[i][j] = dp[i-1][j]
#                if j >= A[i-1]:
#                    dp[i][j] = max(dp[i][j], dp[i-1][j-A[i-1]] + V[i-1])
#        
#        return dp[len(A)][m]
        
        dp = [0 for _ in range(m+1)]
        
        for i in range(len(A)):
            for j in range(m, 0, -1):
                if j >= A[i]:
                    dp[j] = max(dp[j], dp[j-A[i]] + V[i])
        
        return dp[m]

