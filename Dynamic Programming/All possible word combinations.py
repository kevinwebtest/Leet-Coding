def allWordComb(target, words,memo={}):
  if target in memo:
    return memo[target]
  if target == "":
    return [[]]
  output = []
  for word in words:
    if target.startswith(word) == True:
      sliced = target[len(word):]
      wordCombs = allWordComb(sliced,words,memo)
      if len(wordCombs)>0:
        for wordComb in wordCombs:
          wordComb.insert(0,word)
      output += wordCombs
  memo[target]=output
  return output

print(allWordComb("purple", ["purp", "p", "ur", "le", "purpl"]))
print(allWordComb("abcdef", ["ab", "abc", "cd", "def", "abcd","ef","c"]))
print(allWordComb("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"],{}))
print(allWordComb("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"],{}))
print(allWordComb("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee", "eeeeeeeee"],{}))
