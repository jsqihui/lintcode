class Solution:
    # @param heights: a list of integers
    # @return: an integer
    def maxArea(self, heights):
        # write your code here
        
        # use two pointer, update the lower one and calculate the largest 
        if len(heights) <= 1:
            return 0
        
        start = 0
        end = len(heights) - 1
        maxVolume = 0
        while start < end:
            maxVolume = max(maxVolume, min(heights[start], heights[end]) * (end - start))
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return maxVolume

