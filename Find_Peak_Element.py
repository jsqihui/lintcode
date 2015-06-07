class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        if not A or len(A) <= 2:
            return None
        
        start = 1
        end = len(A) - 2
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] < A[mid-1] and A[mid] > A[mid+1]:
                end = mid
            elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
                start = mid
            elif A[mid] < A[mid-1] and A[mid] < A[mid+1]:
                start = mid
            else:
                return mid
        
        if A[start] > A[start+1] and A[start] > A[start-1]:
            return start
        return end

