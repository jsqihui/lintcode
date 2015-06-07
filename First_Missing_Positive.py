class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        if not A:
            return 1
        maxNum = len(A)
        intMap = [0 for _ in range(len(A) + 2)]
        
        for e in A:
            if e >= 0 and e <= maxNum:
                intMap[e] = 1
        
        for i in range(1, len(intMap)):
            if intMap[i] == 0:
                return i


