class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        s = s.split()
        s = [word for word in reversed(s)]
        return " ".join(s)

