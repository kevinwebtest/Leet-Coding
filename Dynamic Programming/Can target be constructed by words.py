# Can the list words be constructed to make the word 'target'
def canWordComb(target, words, memo={}):
  if target in memo:
    return memo[target]
  if target == "":
    return True
  for word in words:
    if target.startswith(word) == True:
      sliced = target[len(word):]
      canWC = canWordComb(sliced, words, memo)
      memo[target] = canWC
      if canWC == True:
        return True
  return False

# or
def canWordComb(target, words, memo={}):
  if target in memo:
    return memo[target]
  if target == "":
    return True
  for word in words:
    if target.startswith(word) == True:
      sliced = target[len(word):]
      canWC = canWordComb(sliced, words, memo)
      if canWC == True:
        memo[target] = True
        return True
  memo[target] = False
  return False


print(canWordComb("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canWordComb("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canWordComb("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee", "eeeeeeeee"]))
