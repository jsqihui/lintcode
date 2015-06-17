class Solution:
    """
    @param A: An integer array.
    @param k: A positive integer (k <= length(A))
    @param target: Integer
    @return a list of lists of integer 
    """
    def kSumII(self, A, k, target):
        # write your code here
        # two pointers
        A = sorted(A)
        ret = []
        self.dfs(A, ret, [], target, k)
        return ret
    
    def dfs(self, A, ret, stack, target, k, pos=0):
        if target < 0 or k < 0:
            return 
        if k == 0 and target == 0:
            ret.append(stack[:])
            return
        
        for i in range(pos, len(A)):
            target = target - A[i]
            k = k - 1
            stack.append(A[i])
            self.dfs(A, ret, stack, target, k, i+1)
            stack.pop()
            k = k + 1
            target = target + A[i]
            
