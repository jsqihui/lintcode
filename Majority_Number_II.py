class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        number1 = None
        number2 = None
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            key = nums[i]
            if key == number1:
                count1 += 1
            elif key == number2:
                count2 += 1
            elif count1 == 0:
                number1 = key
                count1 = 1
            elif count2 == 0:
                number2 = key
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            if number1 == nums[i]:
                count1 += 1
            elif number2 == nums[i]:
                count2 += 1
        
        if count1 > count2:
            return number1
        else:
            return number2


