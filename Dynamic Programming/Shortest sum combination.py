# (?) Jawaban error/salah padahal syntax sama persis dengan yg javascript 
def shortestSumComb(target, numbers, memo={}):
  if target in memo:
    return memo[target]
  if target==0:
    return []
  if target<0:
    return None

  shortestComb = None
  for num in numbers:
    remainder = target - num
    currentComb = shortestSumComb(remainder, numbers, memo)
    memo[remainder] = currentComb
    if currentComb != None:
      currentComb.append(num)
      if (shortestComb==None or len(currentComb)<len(shortestComb)):
        shortestComb = currentComb.copy()
  return shortestComb
    
memo={}
print(shortestSumComb(7,[2,3],memo),memo) #[3, 2, 2]
memo={}
print(shortestSumComb(7,[5,3,4,7],memo),memo) #[7]
memo={}
print(shortestSumComb(8,[1,4,5],memo),memo) #[4, 4]
print(shortestSumComb(7,[4,2],{})) #None
print(shortestSumComb(300,[14,7,15],{})) #None
