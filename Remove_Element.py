class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        
        slow = 0
        fast = 0
        while fast < len(A):
            if A[slow] == elem:
                if A[fast] != elem:
                    A[slow], A[fast] = A[fast], A[slow]
                    slow += 1
                fast += 1
            else:
                slow += 1
                fast += 1
        
        return slow

