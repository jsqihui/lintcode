class Solution:
    # @param s : A string
    # @return : An integer
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if k == 0:
            return 0
        hash = {}
        slow = 0
        fast = 0
        max_length = 0
        while fast < len(s):
            if s[fast] in hash:
                hash[s[fast]] += 1
            else:
                if len(hash) == k:
                    while slow <= fast:
                        hash[s[slow]] -= 1
                        if hash[s[slow]] == 0:
                            break
                        slow += 1
                    hash.pop(s[slow])
                    slow += 1
                hash[s[fast]] = 1
            max_length = max(max_length, fast - slow + 1)
            fast += 1
        
        return max_length

