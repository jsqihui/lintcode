class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        
        # search row
        start = 0
        end = m
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[mid][0] > target:
                end = mid
            elif matrix[mid][0] < target:
                start = mid
            else:
                return True
        
        if matrix[end][0] < target:
            line = end
        else:
            line = start
        
        # search column
        start = 0
        end = n
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[line][mid] > target:
                end = mid
            elif matrix[line][mid] < target:
                start = mid
            else:
                return True
        
        if matrix[line][end] == target:
            return True
        if matrix[line][start] == target:
            return True
        
        return False
        
        


