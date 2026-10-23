class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for r in range(9):
            row_d = {}
            col_d = {}
            for c in range(9):
                if board[r][c] in row_d:
                    if board[r][c]=='.':
                        row_d[board[r][c]]+=1
                    else:
                        return False
                
                else:
                    row_d[board[r][c]] = 1
                
                if board[c][r] in col_d:

                    if board[c][r]=='.':
                        col_d[board[c][r]]+=1
                    else:
                        return False    

                else:
                    col_d[board[c][r]] = 1
        
        for i in range(3):
            for j in range(3):
                matrix_d={}
                for r in range(3):
                    for c in range(3):
                        if board[r+3*i][c + 3*j] in matrix_d:
                            if board[r+3*i][c + 3*j]=='.':
                                matrix_d[board[r+3*i][c + 3*j]]+=1
                            else:
                                return False
                        else:
                            matrix_d[board[r + 3*i][c + 3*j]] = 1
        
        return True
