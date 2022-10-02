# Recursive version
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
    if currentComb != None:
      currentComb.append(num)
      if (shortestComb==None or len(currentComb)<len(shortestComb)):
        shortestComb = currentComb.copy()
  memo[target] = shortestComb
  return shortestComb
    
memo={}
print(shortestSumComb(7,[2,3],memo),memo) #[3, 2, 2]
memo={}
print(shortestSumComb(7,[5,3,4,7],memo),memo) #[7]
memo={}
print(shortestSumComb(8,[1,4,5],memo),memo) #[4, 4]
print(shortestSumComb(7,[4,2],{})) #None
print(shortestSumComb(300,[14,7,15],{})) #None

# Tabular version
def bestSumComb(target, numbers):
  combination = [None for i in range(target+1)]
  combination[0] = []
  for x in range(target+1):
    if combination[x] != None:
      for num in numbers:
        if x+num<=target:
          if (combination[x+num]!= None) and len(combination[x] + [num]) > len(combination[x+num]):
            continue
          combination[x+num] = combination[x] + [num]
  return combination[target]

print(bestSumComb(7,[2,3])) #[3, 2, 2]
print(bestSumComb(7,[5,3,4,7])) #[7]
print(bestSumComb(7,[4,2])) #None
print(bestSumComb(8,[2,3,5])) #[3,5]
print(bestSumComb(300,[14,7])) #None
