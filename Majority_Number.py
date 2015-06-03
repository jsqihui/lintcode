class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        if not nums:
            return None

        majority = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                majority = nums[i]
                count = 1
            else:
                if nums[i] == majority:
                    count += 1
                else:
                    count -= 1
        
        return majority


