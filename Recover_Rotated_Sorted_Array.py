class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        # three flips
        if len(nums) <= 1:
            return nums
        if nums[0] < nums[-1]:
            return nums

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                break
        
        self.reverse(nums, 0, i)
        self.reverse(nums, i + 1, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
        
    
    def reverse(self, nums, i, j):
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
