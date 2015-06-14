class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return A[0]
        if len(A) == 2:
            return max(A[0], A[1])
        dp = [0 for _ in range(len(A))]
        dp[0] = A[0]
        dp[1] = max(A[0], A[1])
        
        for i in range(2, len(A)):
            dp[i] = max(dp[i-2] + A[i], dp[i-1])
        
        return dp[len(A)-1]

