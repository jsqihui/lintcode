class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        # compare from back to front
        endA = m - 1
        endB = n - 1
        last = m + n - 1
        while endA >= 0 and endB >= 0:
            if A[endA] < B[endB]:
                A[last] = B[endB]
                last -= 1
                endB -= 1
            else:
                A[last] = A[endA]
                last -= 1
                endA -= 1
        
        while endB >= 0:
            A[last] = B[endB]
            last -= 1
            endB -= 1
