class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        
#        dp = [[False for _ in range(m+1)] for _ in range(len(A)+1)]
#        for i in range(m):
#            dp[0][i] = False
#        for i in range(len(A)):
#            dp[i][0] = True
#        
#        for i in range(1, len(A)+1):
#            for j in range(1, m+1):
#                dp[i][j] = dp[i-1][j]
#                if j >= A[i-1]:
#                    dp[i][j] = dp[i][j] or dp[i-1][j - A[i-1]]
#        
#        for j in range(m, 0, -1):
#            if dp[len(A)][j]:
#                return j
#        
#        return 0

# the following is TLE and sure how to improve        
        dp = [False for _ in range(m+1)]
        dp[0] = True

        for i in xrange(len(A)):
            for j in xrange(m, 0, -1):
                if j >= A[i]:
                    dp[j] = dp[j] or dp[j - A[i]]
        
        for i in xrange(m, 0, -1):
            if dp[i]:
                return i
        return 0

