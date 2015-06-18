class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # write your code here
        hashmap = {num[i]: False for i in range(len(num))}
        maxLength = 0
        for key in hashmap:
            if hashmap[key]:
                continue
            # find left
            left = key - 1
            right = key + 1
            while left in hashmap and hashmap.get(left) is False:
                hashmap[left] = True
                left = left - 1
            while right in hashmap and hashmap.get(right) is False:
                hashmap[right] = True
                right = right + 1
            
            maxLength = max(maxLength, right - left - 1)
        
        return maxLength

