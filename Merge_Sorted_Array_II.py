ass Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        if not A:
            return B
        if not B:
            return A
        
        a = 0
        b = 0
        ret = []
        while a < len(A) and b < len(B):
            if A[a] > B[b]:
                ret.append(B[b])
                b += 1
            else:
                ret.append(A[a])
                a += 1
        
        while a < len(A):
            ret.append(A[a])
            a += 1
        while b < len(B):
            ret.append(B[b])
            b += 1
        
        return ret
        

