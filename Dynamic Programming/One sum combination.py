# Recursive version
def oneSumComb(target, numbers, memo={}):
  if target in memo:
    return memo[target]
  if target == 0:
    return []
  if target < 0:
    return None
  for num in numbers:
    remainder = target - num
    output = oneSumComb(remainder, numbers, memo)
    if output != None:
      output.append(num)
      memo[target] = output
      return output
  memo[target] = None
  return None

print(oneSumComb(7,[2,3],{})) #[3, 2, 2]
print(oneSumComb(7,[5,3,4,7],{})) #[4, 3]
print(oneSumComb(7,[4,2],{})) #None
print(oneSumComb(300,[14,7],{})) #None

# Tabular version
def oneSumComb(target, numbers):
  combination = [None for i in range(target+1)] #for initialization
  combination[0] = []
  for x in range(target+1):
    if combination[x]!= None:
      for num in numbers:
        if x+num<=target:
          combination[x+num] = combination[x]+[num]
  return combination[target]

print(oneSumComb(7,[2,3])) #[3, 2, 2]
print(oneSumComb(7,[5,3,4,7])) #[4, 3]
print(oneSumComb(7,[4,2])) #None
print(oneSumComb(8,[2,3,5])) #[2,2,2,2]
print(oneSumComb(300,[14,7])) #None
