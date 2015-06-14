class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if not num:
            return None
        
        if num[-1] > num[0]:
            return num[0]
        
        start = 0
        end = len(num) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if num[mid] > num[0]:
                start = mid
            else:
                end = mid
        
        return min(num[start], num[end])
