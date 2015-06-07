class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        # state dp[i] max sum coins from i till endh for player 1
        # loop from back to front
        
        dp = [0 for _ in range(5)]
        sumValue = 0
        length = len(values)
        for i in reversed(range(length)):
            sumValue += values[i]
            a = b = c = d = 0
            if i + 1 < length:
                a = values[i+1]
            if i + 2 < length:
                b = dp[(i+2)%5]
            if i + 3 < length:
                c = dp[(i+3)%5]
            if i + 4 < length:
                d = dp[(i+4)%5]
            
            dp[i%5] = max(values[i] + min(b, c), values[i] + a + min(c, d))
        
        return dp[0] > sumValue - dp[0]


