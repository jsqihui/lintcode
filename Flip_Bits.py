""" it is very tricky to do bit manipulation in python """
class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        count = 32
        c = a ^ b
        ret = 0
        while count > 0:
            ret += c & 1
            c = c >> 1
            count = count - 1

        return ret
