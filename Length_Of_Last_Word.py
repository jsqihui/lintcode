class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        # Write your code here
        words = s.strip().split(' ')
        if not words:
            return 0
        return len(words[-1])
