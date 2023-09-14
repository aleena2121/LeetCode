class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res= set()
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    temp= board[i][j]
                    if (i, temp) in res or (temp, j) in res or (i//3, j//3, temp) in res:
                        return False
                    res.add((i, temp))
                    res.add((temp, j))
                    res.add((i//3, j//3, temp))
        return True