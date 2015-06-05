class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if not A:
            return 0
        
        if target <= A[0]:
            return 0
        if target > A[-1]:
            return len(A)
        
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid
        
        if A[start] == target:
            return start
        return end

