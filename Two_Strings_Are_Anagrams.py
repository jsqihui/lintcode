class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        # bit map?
        if len(s) != len(t):
            return False
        
        bitmap = [0 for _ in range(256)]
        
        for e in s:
            bitmap[ord(e)] += 1
        
        for e in t:
            bitmap[ord(e)] -= 1
            if bitmap[ord(e)] < 0:
                return False
        
        return True

