class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        # Write your code here
        if n == 1:
            return '1'
        current = '1'
        for i in range(1, n):
            current = self.translate(current)
        
        return current
    
    def translate(self, current):
        i = 1
        ret = ""
        char = current[0]
        count = 1
        while i < len(current):
            if current[i] == char:
                count += 1
            else:
                ret += str(count) + char
                char = current[i]
                count = 1
            i += 1
        ret += str(count) + char
        return ret
