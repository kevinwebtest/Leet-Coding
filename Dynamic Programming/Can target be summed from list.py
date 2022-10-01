# Check if the list numbers can added up to the target (Every number can be used more than once)
# Recursive version
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

# Tabular version
print(canSum(7,[2,3],{}) #True
print(canSum(7,[4,2],{}) #False
# Hati-hati karena python ingat memo/dictionary yang di dalam function ketika pemanggilan selanjutnya jika memo dikosongkan saat pemanggilan function
memo ={}
print(canSum(300,[14,7],memo),memo) #False
