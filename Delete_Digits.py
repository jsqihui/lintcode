class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write you code here
        # loop from index 0, find the min number for current position
        # which mean if cur number larger than following one, delete
        # the cur number
        if len(A) == k:
            return ''
        
        for i in range(k):
            for j in range(len(A)):
                if j == len(A) - 1 or A[j] > A[j+1]:
                    A = A[:j] + A[j+1:]
                    break
        
        for i in range(len(A)):
            if A[i] != '0':
                break
        
        return A[i:]
