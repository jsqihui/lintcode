class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        if len(triangle) <= 1:
            return triangle[0][0]
        row = [sys.maxint for _ in range(len(triangle[-1]))]
        row[0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in reversed(range(1, len(triangle[i]))):
                row[j] = triangle[i][j] + min(row[j], row[j-1])
            row[0] += triangle[i][0]
        
        return min(row)

