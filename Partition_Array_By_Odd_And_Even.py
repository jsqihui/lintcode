class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        end = len(nums) - 1
        start = 0
        
        while start <= end:
            if nums[start] % 2 == 0:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1
