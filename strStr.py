class Solution:
    def strStr(self, source, target):
        # write your code here
        if target is None or source is None:
            return -1
        for i in range(len(source) - len(target) + 1):
            j = 0
            while j < len(target):
                if source[i+j] != target[j]:
                    break
                j += 1
            if j == len(target):
                return i
        
        return -1

