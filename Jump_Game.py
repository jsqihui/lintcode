class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        # for current one, jump max
        i = 0
        current_pos = 1
        while i < current_pos:
            current_pos = max(A[i] + i, current_pos)
            if current_pos >= len(A) - 1:
                return True
            i += 1
        return False

