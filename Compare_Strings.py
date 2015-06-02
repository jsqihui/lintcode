class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        if len(A) < len(B):
            return False
        
        hashmap = {}
        for e in A:
            if e in hashmap:
                hashmap[e] += 1
            else:
                hashmap[e] = 1
        
        for e in B:
            if e not in hashmap:
                return False
            hashmap[e] -= 1
            if hashmap[e] < 0:
                return False
        
        return True
