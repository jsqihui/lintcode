class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if len(A) <= 2:
            return len(A)

        slow = 1
        for i in range(2, len(A)):
            if A[slow] == A[slow - 1] and A[slow] == A[i]:
                continue
            slow += 1
            A[slow] = A[i]
        
        return slow + 1
