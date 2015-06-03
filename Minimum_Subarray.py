class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        nums = [-e for e in nums]
        
        prefixSum = 0
        currentMin = 0
        maxValue = -sys.maxint
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            maxValue = max(prefixSum - currentMin, maxValue)
            currentMin = min(prefixSum, currentMin)
        
        return -maxValue


