# Count all possible path from top left to bottom right
# Recursive version
def twoDimensionalGrid(m,n,smallerGrid={}):
  if m==0 or n==0:
    return 0
  if m==1 or n==1:
    return 1
  mn = str(m) + ',' + str(n)
  if mn in smallerGrid:
    return smallerGrid[mn]
  smallerGrid[mn] = twoDimensionalGrid(m-1,n,smallerGrid) + twoDimensionalGrid(m,n-1,smallerGrid)
  return smallerGrid[mn]
print(twoDimensionalGrid(2,3))

# Tabular version
def allPathGrid(m,n):
  grid = [[0 for y in range(n+1)] for x in range(m+1)]
  grid[1][1] = 1
  for i in range(m+1):
    for j in range(n+1):
      if i+1<=m:
        grid[i+1][j] +=  grid[i][j]
      if j+1<=n:
        grid[i][j+1] +=  grid[i][j]
  return grid[m][n]
print(allPathGrid(99,12)) #383707936014390

