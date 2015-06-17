class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        # use the partition idea
        # find a pivot, and move all element by the pivot
        start = 0
        end = len(A) - 1
        return self.helper(A, start, end, len(A) - k)
    
    def helper(self, nums, low, high, k):
        # 1. use quick sort partition method
        #if k >= 0 and k < high - low + 1:
            # partition with the last element of array
            # and get position of this element in a sorted array
        pos = self.partition(nums, low, high)
        if pos == k:
            return nums[pos]
        elif pos > k:
            return self.helper(nums, low, pos - 1, k)
        else:
            return self.helper(nums, pos + 1, high, k)
    
    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low
        for j in range(low, high):
            if nums[j] <= pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i
        
        
        

