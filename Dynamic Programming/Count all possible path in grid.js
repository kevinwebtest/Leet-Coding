function pathsInGrid(m,n, memo={}) {
  let mn = `${m},${n}`
  if (mn in memo){
      return memo[mn]
  }
  if (m===1 || n===1) {
      return 1
  } 
  memo[mn] = pathsInGrid(m-1,n, memo) + pathsInGrid(m,n-1, memo)
  return memo[mn]
}

console.log(pathsInGrid(99,12)) //383707936014390


function newPathInGrid(m,n) {
  const grid = new Array(m+1).fill().map(()=>new Array(n+1).fill(0))
  grid[1][1] = 1
  for (let i=0; i<m+1; i++) {
      for (let j=0; j<n+1; j++) {
          if(i+1<=m) {
              grid[i+1][j] += grid[i][j] 
          }
          if(j+1<=n) {
              grid[i][j+1] += grid[i][j] 
          }
      }
  }
  return grid[m][n]
}

console.log(newPathInGrid(99,12)) //383707936014390