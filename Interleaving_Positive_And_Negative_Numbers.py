class Solution:
    """
    @param A: An integer array.
    @return nothing
    """
    def rerange(self, A):
        """
        >>>rerange([-1, -2, -3, 4, 5, 6])
        [-1, 5, -2, 4, -3, 6]
        """
        # use two pointers, the slower one point to the negative
        # fast one point to the positive
        # 1. use pivot 0 to do a quick sort
        start = 0
        end = len(A) - 1
        while start < end:
            while start < end and A[start] < 0:
                start += 1
            while start < end and A[end] > 0:
                end -= 1
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1
        
        # find pos start
        for i in range(len(A)):
            if A[i] > 0:
                break
        posStart = i
        if posStart >= len(A) - posStart:
            negStart = 1
        else:
            negStart = 0
        while negStart < posStart and posStart < len(A) and A[negStart] < 0:
            A[negStart], A[posStart] = A[posStart], A[negStart]
            negStart += 2
            posStart += 1
