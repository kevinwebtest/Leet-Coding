var rotate = function(matrix) {
    const mLen = matrix.length
    const depth = ~~(mLen/2)
    for(let i=0; i<depth; i++) {
        const colLen = mLen-1-i*2
        const opp = mLen-1-i
        for(let j=0; j<colLen; j++) {
            const temp = matrix[i][i+j]
            matrix[i][i+j] = matrix[opp-j][i]
            matrix[opp-j][i] = matrix[opp][opp-j]
            matrix[opp][opp-j] = matrix[i+j][opp]
            matrix[i+j][opp] = temp
        }
    }
    return matrix
};