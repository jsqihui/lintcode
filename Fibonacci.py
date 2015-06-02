class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        if n <= 2:
            return n - 1
        fib = [0, 1]
        
        for i in range(2, n):
            fib[i%2] = fib[(i-1)%2] + fib[(i-2)%2]
        
        return fib[(n - 1)%2]
