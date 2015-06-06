class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        count = 0 
        while n > 0 :
            n = n / 5
            count += n
        
        return count
