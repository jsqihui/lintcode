class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if not numbers or len(numbers) < 3:
            return []

        numbers = sorted(numbers)
        ret = []
        for i in range(len(numbers)):
            target = -numbers[i]
            start = i + 1
            end = len(numbers) - 1
            while start < end:
                s = numbers[start] + numbers[end]
                if s == target:
                    cur = [numbers[i], numbers[start], numbers[end]]
                    if cur not in ret:
                        ret.append(cur)
                    start += 1
                    end -= 1
                elif s > target:
                    end -= 1
                else:
                    start += 1
            
        return ret

