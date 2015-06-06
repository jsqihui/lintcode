class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers = sorted(numbers)

        minDist = sys.maxint
        ret = 0
        for i in range(len(numbers)):
            start = i + 1
            end = len(numbers) - 1
            while start < end:
                total = numbers[i] + numbers[start] + numbers[end]
                if total == target:
                    return target
                elif total > target:
                    if minDist > total - target:
                        minDist = total - target
                        ret = total
                    end -= 1
                else:
                    if minDist > target - total:
                        minDist = target - total
                        ret = total
                    start += 1
        
        return ret
                    

