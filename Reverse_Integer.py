class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        flag = 1
        x = n
        if x < 0:
            flag = -1
        
        x = str(abs(x))
        x = x[::-1]
        if int(x) > 2**32 - 1:
            return 0
        return flag * int(x)

