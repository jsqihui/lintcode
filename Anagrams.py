class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        # sort strs first
        if not strs or len(strs) <= 1:
            return []
        sorted_strs = [''.join(sorted(s)) for s in strs]
        hashmap = {}
        for i in range(len(sorted_strs)):
            s = sorted_strs[i]
            if s in hashmap:
                hashmap[s] += 1
            else:
                hashmap[s] = 1

        ret = []
        for i in range(len(sorted_strs)):
            if hashmap[sorted_strs[i]] > 1:
                ret.append(strs[i])

        return ret

