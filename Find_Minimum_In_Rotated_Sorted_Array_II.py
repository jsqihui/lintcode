class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if not num:
            return None
        start = 0
        end = len(num) - 1
        while start + 1 < end:
            if num[start] < num[end]:
                return num[start]
            
            mid = start + (end - start)/2
            if num[mid] < num[end]:
                end = mid
            elif num[mid] > num[start]:
                start = mid
            else:
                start = start + 1
                
        return min(num[start], num[end])

