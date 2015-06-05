class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        # bitmap - fake
        bitmap = [0 for _ in range(256)]
        for i in range(len(str)):
            index = ord(str[i])
            if bitmap[index]:
                return False
            else:
                bitmap[index] = 1
        return True

