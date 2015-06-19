class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        # write your code here
        if not s:
            return 0
        hashmap = {}
        start = -1
        end = 0
        max_length = 0
        while end < len(s):
            if s[end] in hashmap and start < hashmap[s[end]]:
                start = hashmap[s[end]]
            max_length = max(max_length, end - start)
            hashmap[s[end]] = end
            end += 1
        
        return max_length
                

