class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        if len(A) <= 1:
            return [1]
        cur = 1
        left = []
        for e in A:
            cur *= e
            left.append(cur)
        
        cur = 1
        right = []
        for e in A[::-1]:
            cur *= e
            right = [cur] + right
            
        ret = A[:]
        ret[0] = right[1]
        ret[-1] = left[-2]
        for i in range(1, len(A)-1):
            ret[i] = left[i-1] * right[i+1]
        
        return ret
