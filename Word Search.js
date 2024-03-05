var exist = function(board, word) {
    const dfs = (i, j, idx, newBoard) => {
        if(isFound) return
        if(idx===word.length) {
            isFound = true
            return
        }
        if(i<0 || i>=newBoard.length || j<0 || j>=newBoard[0].length || newBoard[i][j]!==word[idx]) {
            return
        }
        const newerBoard = newBoard.map(innerArray=>[...innerArray])
        newerBoard[i][j] = "-"
        dfs(i+1,j, idx+1, newerBoard)
        dfs(i-1,j, idx+1, newerBoard)
        dfs(i,j+1, idx+1, newerBoard)
        dfs(i,j-1, idx+1, newerBoard)
    }
    let isFound = false
    
    outerloop: for(let i=0; i<board.length; i++){
        for(let j=0; j<board[0].length; j++) {
            if(board[i][j]===word[0]) {
                dfs(i,j, 0, board)
                if(isFound){
                    break outerloop
                }
            } 
        }
    }
    return isFound
};

console.log(exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))