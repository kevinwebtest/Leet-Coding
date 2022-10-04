class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]
        for x in range(rowIndex):
            row = [i+j for i, j in zip([0]+row, row+[0])]
        return row
