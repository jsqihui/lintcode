class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        for i in reversed(range(len(A)/2 + 1)):
            self.siftdown(A, i)
    
    def siftdown(self, A, k):
        while k < len(A):
            smallest = k
            if k * 2 + 1 < len(A) and A[k * 2 + 1] < A[smallest]:
                smallest = k * 2 + 1
            if k * 2 + 2 < len(A) and A[k * 2 + 2] < A[smallest]:
                smallest = k * 2 + 2
            if smallest == k:
                break
            A[k], A[smallest] = A[smallest], A[k]
            k = smallest
