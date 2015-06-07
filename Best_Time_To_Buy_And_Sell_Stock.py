class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        # find max till now and min till now
        
        maxProfit = 0
        maxNow = -sys.maxint
        minNow = sys.maxint
        for i in range(len(prices)):
            maxNow = max(maxNow, prices[i])
            if minNow > prices[i]:
                maxNow = prices[i]
                minNow = prices[i]
            maxProfit = max(maxProfit, maxNow - minNow)
        
        return maxProfit

