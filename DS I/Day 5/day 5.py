class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
             #checking rows
        
        for x in range(len(board)):
            lst = []
            for y in range(len(board[x])):
                if board[x][y] == "." : continue
                if board[x][y] in lst : return False
                lst.append(board[x][y])
        
        
        #checking Columns
        
        for x in range(len(board)):
            lst = []
            for y in range(len(board[x])):
                if board[y][x] == "." : continue
                if board[y][x] in lst : return False
                lst.append(board[y][x])
        
        
        #checking 3x3 sub-boxes
        
        for x in range(0, len(board), +3):
            for y in range(0, len(board), +3):
                
                lst = []
                
                for i in range(3):
                    for j in range(3):
                        
                        
                        if board[i+x][j+y] == "." : continue
                        if board[i+x][j+y] in lst : return False
                        lst.append(board[i+x][j+y])
        
        #if all passes
        return True
   