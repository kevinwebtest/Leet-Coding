var generateMatrix = function(n) {
    let horiStart = 0
    let horiEnd = n-1
    let vertiStart = 0
    let vertiEnd = n-1
    let direction = 0
    let num = 1
    const matrix = new Array(n).fill().map(() => new Array(n).fill(0))
    while(horiStart<=horiEnd && vertiStart<=vertiEnd) {
        if(direction===0) {
            for(let i=horiStart; i<=horiEnd; i++){
                matrix[vertiStart][i] = num
                num+=1
            }
            vertiStart+=1
        }
        else if(direction===1) {
            for(let i=vertiStart; i<=vertiEnd; i++){
                matrix[i][horiEnd] = num
                num+=1
            }
            horiEnd-=1
        }
        else if(direction===2) {
            for(let i=horiEnd; i>=horiStart; i--){
                matrix[vertiEnd][i] = num
                num+=1
            }
            vertiEnd-=1
        }
        else {
            for(let i=vertiEnd; i>=vertiStart; i--){
                matrix[i][horiStart] = num
                num+=1
            }
            horiStart+=1
        }
        direction=(direction+1)%4
    }
    return matrix
};

console.log(generateMatrix(3))