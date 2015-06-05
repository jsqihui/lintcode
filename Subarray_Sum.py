class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        
        prefixSum = 0
        sumMap = {}
        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum == 0:
                return [0, i]
            if prefixSum in sumMap:
                return [sumMap[prefixSum]+1, i]
            else:
                sumMap[prefixSum] = i
        
        

