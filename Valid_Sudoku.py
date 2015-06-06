class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        ret = True
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                ret = ret and self.validCell(board, i, j)
        
        return ret and self.validRow(board) and self.validCol(board)
    
    def validRow(self, board):
        for i in range(9):
            nums = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in nums:
                    return False
                else:
                    nums.add(board[i][j])
        return True
    
    def validCol(self, board):
        for i in range(9):
            nums = set()
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in nums:
                    return False
                else:
                    nums.add(board[j][i])
        return True
    
    def validCell(self, board, row_start, col_start):
        nums = set()
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if board[i][j] != '.' and board[i][j] in nums:
                    return False
                else:
                    nums.add(board[i][j])
        return True
