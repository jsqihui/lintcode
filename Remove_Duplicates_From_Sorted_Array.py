class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        
        slow = 0
        fast = 1
        while fast < len(A):
            value = A[slow]
            if value == A[fast]:
                fast += 1
                continue
            else:
                slow += 1
                A[slow], A[fast] = A[fast], A[slow]
                fast += 1
        
        return slow + 1
            
          

