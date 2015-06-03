class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        # write your code here
        return self.helper1(nums, 0, len(nums) - 1, (len(nums) - 1) / 2)
    
    def helper1(self, nums, low, high, k):
        # 1. use quick sort partition method
        #if k >= 0 and k < high - low + 1:
            # partition with the last element of array
            # and get position of this element in a sorted array
        pos = self.partition(nums, low, high)
        if pos == k:
            return nums[pos]
        elif pos > k:
            return self.helper1(nums, low, pos - 1, k)
        else:
            return self.helper1(nums, pos + 1, high, k)
    
    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low
        for j in range(low, high):
            if nums[j] <= pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i

