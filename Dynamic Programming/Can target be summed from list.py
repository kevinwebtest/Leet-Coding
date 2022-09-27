# Check if the list numbers can added up to the target (Every number can be used more than once)
def canSum(target, numbers, memo = {}):
  if target in memo:
    return memo[target]
  if target==0:
    return True
  if target<0:
    return False

  for num in numbers:
    remainder = target - num
    if canSum(remainder, numbers, memo)==True:
      memo[target] = True
      return True
  memo[target] = False
  return False

# Second code
def canSum(target, numbers, memo = {}):
  if target in memo:
    return memo[target]
  if target==0:
    return True
  if target<0:
    return False

  for num in numbers:
    remainder = target - num
    memo[remainder] = canSum(remainder, numbers, memo)
    if memo[remainder]==True:
      return True
  return False

memo ={}
print(canSum(7,[2,3],memo),memo) #True
memo ={}
print(canSum(7,[4,2],memo),memo) #False
memo ={}
print(canSum(300,[14,7],memo),memo) #False
