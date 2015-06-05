class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        # Write your code here
        
        hashmap = {'{':'}', '(':')', '[':']'}
        stack = []
        
        for i in range(len(s)):
            if s[i] in hashmap.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                symbol = stack.pop()
                if symbol not in hashmap or hashmap[symbol] != s[i]:
                    return False
        
        if stack:
            return False
        return True
    

