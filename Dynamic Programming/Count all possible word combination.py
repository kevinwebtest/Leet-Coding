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
