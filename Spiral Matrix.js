/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    const output=[]
    if (matrix.length===0) {
        return output
    }
    let row_start = 0
    let col_start = 0
    let row_end = matrix.length-1
    let col_end = matrix[0].length-1
    while (row_start<=row_end && col_start<=col_end) {
        for(let i=col_start; i<col_end+1; i++) {
            output.push(matrix[row_start][i])
        } 
        row_start += 1
        for(let i=row_start; i<row_end+1; i++) {
            output.push(matrix[i][col_end])
        } 
        col_end -= 1
        if (row_start<=row_end) {
            for(let i=col_end; i>col_start-1; i--) {
                output.push(matrix[row_end][i])
            } 
            row_end -= 1
        }
        if (col_start<=col_end) {
            for(let i=row_end; i>row_start-1; i--) {
                output.push(matrix[i][col_start])
            } 
            col_start += 1
        }
    }
    return output
};