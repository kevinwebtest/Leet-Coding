# Return the amount of possible word combinations for a word target
# Recursive version
def countWordComb(target, words, memo={}):
  if target in memo:
    return memo[target]
  if target == "":
    return 1
  counter = 0
  for word in words:
    if target.startswith(word) == True:
      sliced = target[len(word):]
      ifCount = countWordComb(sliced, words, memo)
      counter += ifCount
  memo[target] = counter
  return counter
print(countWordComb("purple", ["purp", "p", "ur", "le", "purpl"],{}))
print(countWordComb("abcdef", ["ab", "abc", "cd", "def", "abcd"],{}))
print(countWordComb("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"],{}))
print(countWordComb("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"],{}))
print(countWordComb("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee", "eeeeeeeee", "f"],{}))

# Tabular version
def countConstruct(target, words):
  countTarget = [0 for i in range(len(target)+1)]
  countTarget[0] = 1
  for x in range(len(countTarget)):
    if countTarget[x] > 0:
      for word in words:
        if target[x:x+len(word)] == word:
          countTarget[x+len(word)] += countTarget[x]
  return countTarget[len(target)]

print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee", "eeeeeeeee"]))
