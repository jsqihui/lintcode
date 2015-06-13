class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        # Write your code here
        # 
        if len(A) == 1:
            return [0, 0]
        
        sumValue = A[0]
        maxValue = sumValue
        start = 0
        ret = [0, 0]
        for i in range(1, len(A)):
            if sumValue < 0:
                sumValue = 0
                start = i

            sumValue += A[i]
            if maxValue < sumValue:
                maxValue = sumValue
                ret = [start, i]
        
        return ret

