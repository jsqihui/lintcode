class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        # from left to right
        if not A:
            return 0
        dp = 1
        max_left = 1
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                dp += 1
            else:
                dp = 1
            max_left = max(dp, max_left)

        dp = 1
        max_right = 1
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                dp += 1
            else:
                dp = 1
            max_right = max(dp, max_right)

        return max(max_left, max_right)

