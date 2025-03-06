class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        def backtrack(i,j,index):
            if index == len(word):
                return True
            if i<0 or j<0 or i>=row or j>=col or board[i][j]!=word[index]:
                return False
            
            temp = board[i][j]
            board[i][j] = "#"

            found = backtrack(i,j-1,index+1) or backtrack(i,j+1,index+1) or backtrack(i+1,j,index+1) or backtrack(i-1,j,index+1)

            board[i][j] = temp
            return found
        
        for i in range(row):
            for j in range(col):
                if backtrack(i,j,0):
                    return True
            
        return False