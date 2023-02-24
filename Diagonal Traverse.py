class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diag = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j in diag:
                    diag[i+j].append(mat[i][j])
                else:
                    diag[i+j] = [mat[i][j]]
        diaglist = []
        for key in diag:
            if key%2==0:
                diag[key].reverse()
            diaglist += diag[key]
        return diaglist
