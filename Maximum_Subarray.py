class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        
        minSum = 0
        maxSub = -sys.maxint
        prefixSum = 0
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            maxSub = max(maxSub, prefixSum - minSum)
            minSum = min(minSum, prefixSum)
        
        return maxSub
