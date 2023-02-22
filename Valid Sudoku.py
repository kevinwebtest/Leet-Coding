class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        block = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if i not in row:
                    row[i] = [board[i][j]]
                else:
                    if board[i][j] in row[i]:
                        return False
                    else:
                        row[i].append(board[i][j])
                if j not in col:
                    col[j] = [board[i][j]]
                else:
                    if board[i][j] in col[j]:
                        return False
                    else:
                        col[j].append(board[i][j])
                m = i//3
                n = j//3
                ij = str(m) + str(n)
                if ij not in block:
                    block[ij] = [board[i][j]]
                else:
                    if board[i][j] in block[ij]:
                        return False 
                    else:
                        block[ij].append(board[i][j])

        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        data = []
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num!=".":
                    data += [(num, i), (j,num), (i//3, j//3, num)]
        return len(data)==len(set(data))