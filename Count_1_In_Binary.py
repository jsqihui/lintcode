class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        count = 0
        while num > 0:
            count += 1
            # find tailing 1 in num and change it to 0
            num = num & num - 1
        
        return count
