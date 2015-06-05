class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        ret = 0
        for i in A:
            ret = ret ^ i
        
        return ret

