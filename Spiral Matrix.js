/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    let startCol = 0
    let endCol = matrix[0].length -1
    let startRow = 0
    let endRow = matrix.length - 1 

    const output = []
    while (startCol <= endCol && startRow <= endRow) {
        for(let i=startCol; i<=endCol; i++) {
            output.push(matrix[startRow][i])
        }
        startRow+=1
        for(let i=startRow; i<=endRow; i++) {
            output.push(matrix[i][endCol])
        }
        endCol-=1
        if(startRow<=endRow) {
            for(let i=endCol; i>=startCol; i--) {
                output.push(matrix[endRow][i])
            }
            endRow-=1
        }
        if(startCol<=endCol) {
            for(let i=endRow; i>=startRow; i--) {
                output.push(matrix[i][startCol])
            }
            startCol+=1
        }
    }
    return output
};