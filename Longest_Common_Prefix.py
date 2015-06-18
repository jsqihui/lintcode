class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        lcp = ""
        if not strs:
            return lcp
        flag = True
        minLength = min([len(s) for s in strs])
        for i in range(minLength):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    flag = False
                    break
            if flag:
                lcp += char
            else:
                break
        
        return lcp

