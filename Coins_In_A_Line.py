class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        if n == 0:
            return False
        if n <= 2:
            return True
        
        dp = [False for _ in range(3)]
        dp[1] = True
        dp[2] = True
# Memory exceeds the limit if uncomment the following two lines, doesn't make much sense        
#        for i in xrange(3, n + 1):
#            dp[i % 3] = dp[(i - 3) % 3]
        
        return dp[n % 3]
