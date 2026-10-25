class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

    #    c = {}
       
        for i in range(len(board)):
            r = {}
            c = {}
            for j in range(len(board[i])):
                if (board[i][j] in r and board[i][j]!='.') or (board[j][i] in c and board[j][i]!='.'):
                    print('yes')
                    return False
                
                else:
                    r[board[i][j]] = 1
                    c[board[j][i]] = 1
        
        row = 3
        col = 3
        
        while True:
            matrix={}
            for i in range(row-3, row):
                for j in range(col-3, col):
                    if board[i][j] in matrix and board[i][j]!='.':
                        return False
                    else:

                        matrix[board[i][j]] = 1
            col+=3
            if col == 12:
                if row == 9:
                    return True
                
                else:
                    col = 3
                    row+=3

            


