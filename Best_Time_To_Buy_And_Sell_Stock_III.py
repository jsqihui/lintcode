class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0
        
        prefixMax = [0 for _ in range(len(prices))]
        preMin = prices[0]
        postfixMax = prefixMax[:]
        postMax = prices[len(prices)-1]
        maxProfit = 0
        
        for i in range(1, len(prices)):
            preMin = min(preMin, prices[i])
            prefixMax[i] = max(prefixMax[i-1], prices[i] - preMin)
        
        for i in range(len(prices) - 2, -1, -1):
            postMax = max(postMax, prices[i])
            postfixMax[i] = max(postfixMax[i+1], postMax - prices[i])
        
        for i in range(len(prices)):
            maxProfit = max(prefixMax[i]+postfixMax[i], maxProfit)
        
        return maxProfit
