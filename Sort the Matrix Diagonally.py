class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        line = len(mat)
        row = len(mat[0])
        def diagonal(i,j):
            val = []
            while i<line and j<row:
                val.append(mat[i][j])
                i+=1
                j+=1
            val.sort()
            while i and j:
                i-=1
                j-=1
                mat[i][j] = val.pop()
        for i in range(line):
            diagonal(i,0)
        for j in range(row):
            diagonal(0,j)
        return mat
