class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        # write your code here
        max_length = 0
        ret = []
        for word in dictionary:
            if len(word) == max_length:
                ret.append(word)
            elif len(word) > max_length:
                ret = [word]
                max_length = len(word)
        return ret

