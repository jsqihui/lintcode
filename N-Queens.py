class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.res = []
        self.solve(n, 0, [-1 for i in xrange(n)])
        return self.res
     
    def solve(self, n, currQueenNum, board):
        if currQueenNum == n:
            oneAnswer = [ ['.' for j in xrange(n)] for i in xrange(n) ]
            for i in xrange(n): 
                oneAnswer[i][board[i]] = 'Q'
                oneAnswer[i] = ''.join(oneAnswer[i])
            self.res.append(oneAnswer)
            return
        # try to put a Queen in (currQueenNum, 0), (currQueenNum, 1), ..., (currQueenNum, n-1)
        for i in xrange(n):
            if self.validate(currQueenNum, board, i):
                board[currQueenNum] = i
                self.solve(n, currQueenNum + 1, board)
                board[currQueenNum] = -1
    
    def validate(self, currQueenNum, board, i):
            # test whether board[currQueenNum] can be i or not
            for k in xrange(currQueenNum):
                # check column
                if board[k] == i:
                    return False
                # check dianogal
                if abs(board[k] - i) == currQueenNum - k:
                    return False
            return True
