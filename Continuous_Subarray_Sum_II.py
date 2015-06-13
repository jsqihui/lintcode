class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySumII(self, A):
        # Write your code here
        if not A:
            return None
        if len(A) == 1:
            return [0, 0]
        A = A + A
        
        start = 0
        cur_sum = A[0]
        max_sum = A[0]
        ret = [0, 0]

        for i in range(1, len(A)):
            if cur_sum < 0:
                cur_sum = 0
                start = i
            
            cur_sum += A[i]
            if max_sum < cur_sum:
                max_sum = cur_sum
                ret = [start, i]
        
        if ret[1] >= len(A) / 2:
            ret[1] -= len(A) / 2
        
        return ret
                

