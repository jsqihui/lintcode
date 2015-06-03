class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        if not s:
            return None
        ret = []
        self.dfs(s, ret)
        return ret
        
    def dfs(self, s, ret, stack=[], pos=0):
        if pos == len(s):
            ret.append(stack[:])
            return
        
        for i in range(pos, len(s)):
            if self.isPalindrome(s, pos, i):
                stack.append(s[pos:i+1])
                self.dfs(s, ret, stack, i+1)
                stack.pop()
    
    def isPalindrome(self, s, i, j):
        if i == j:
            return True
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

