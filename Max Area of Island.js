/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function(grid) {
    const dfs = (i, j) => {
        if(i<0 || i>=grid.length || j<0 || j>=grid[0].length || grid[i][j]!==1) {
            return
        }
        grid[i][j] = "-"
        islandSize += 1
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)
    }
    let biggestIsland = 0
    let islandSize
    for(let i=0;i<grid.length; i++) {
        for(let j=0; j<grid[0].length; j++) {
            if(grid[i][j]===1) {
                islandSize = 0 
                dfs(i,j)
                biggestIsland = Math.max(biggestIsland, islandSize)
            }
        }
    }
    return biggestIsland
};

console.log(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])) //6