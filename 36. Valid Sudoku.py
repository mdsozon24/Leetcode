class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()
        for r in range(9):
            for c in range(9):
                if board[r][c] in s and board[r][c]!='.':
                    return False
                else:
                    s.add(board[r][c])
            s = set()
        s = set()
        for c in range(9):
            for r in range(9):
                if board[r][c] in s and board[r][c]!='.':
                    return False
                else:
                    s.add(board[r][c])
            s = set()
        s = set()
        for k in range(0,9,3):
            for p in range(0,9,3):
                for i in range(k,k+3):
                    for j in range(p,p+3):
                        if board[i][j] in s and board[i][j]!='.':
                            return False
                        else:
                            s.add(board[i][j])
                s = set()
        return True