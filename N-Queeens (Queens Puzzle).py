class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pDiag = set()
        nDiag = set()

        output = []
        board = [['.']*n for i in range(n)]

        def row(r):
            if r==n:
                mod = ["".join(row) for row in board]
                output.append(mod)
                return
            
            for c in range(n):
                if (c in col) or ((r+c) in pDiag) or ((r-c) in nDiag):
                    continue
                col.add(c)
                pDiag.add(r+c)
                nDiag.add(r-c)
                board[r][c] = "Q"
                row(r+1)
                col.remove(c)
                pDiag.remove(r+c)
                nDiag.remove(r-c)
                board[r][c] = "."
        row(0)
        return output
