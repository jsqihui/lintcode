ass Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        # sort and use two pointer
        if not numbers or len(numbers) <= 1:
            return []
        nums = sorted(numbers)
        
        start = 0
        end = len(nums) - 1
        num1 = 0
        num2 = 0
        while start < end:
            if nums[start] + nums[end] == target:
                num1 = nums[start]
                num2 = nums[end]
                break
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1
        
        ret = []
        for i in range(len(numbers)):
            if len(ret) == 2:
                break
            if numbers[i] == num1:
                ret.append(i+1)
            elif numbers[i] == num2:
                ret.append(i+1)
        
        return sorted(ret)

