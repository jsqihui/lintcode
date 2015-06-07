class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n   
    """
    def combine(self, n, k):      
        # write your code here  
        self.ret = []
        self.dfs(n, k)
        return self.ret
    
    def dfs(self, n, k, stack = [], pos = 1):
        if len(stack) == k:
            self.ret.append(stack[:])
            return
        
        for i in range(pos, n + 1):
            stack.append(i)
            self.dfs(n, k, stack, i + 1)
            stack.pop()

