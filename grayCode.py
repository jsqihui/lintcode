class Solution:
    # @return a list of integers
    def grayCode1(self, n):
        #The first thing we need to do is to figure out the solution size when given n. we know it is 2^n. Then what we should do is to xor index>>1 and index
        res=[]
        size=1<<n
        for i in range(size):
            res.append((i>>1)^i)
        return res
    
    def grayCode(self, n):
        # when create n + 1, add 1 to n result and reverse then append to n
        ls=[0]
        for i in range(n):
            l=[]
            for num in ls:
                l.append(num+2**i)
            ls+=l[::-1]
        return ls
        
