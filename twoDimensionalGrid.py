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
print(twoDimensionalGrid(18,18))
