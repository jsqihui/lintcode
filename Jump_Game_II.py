class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        max_range = 0
        count = 0
        start = 0
        while max_range < len(A) - 1:
            count = count + 1
            new_start = max_range + 1
            for j in range(start, max_range+1):
                max_range = max(max_range, A[j]+j)
            start = new_start
        
        return count
