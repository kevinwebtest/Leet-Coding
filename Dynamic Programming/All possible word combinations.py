# Return all possible combination of small strings to a target string
# Recursive version
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

# Tabular version
def allConstruct(target,words):
  allCombination = [[] for i in range(len(target)+1)]
  allCombination[0] = [[]]

  for x in range(len(target)):
    if len(allCombination[x]) > 0:
      for word in words:
        if target[x:x+len(word)] == word:
          for oneWordComb in allCombination[x]:
            wordComb = oneWordComb + [word]
            allCombination[x+len(word)] += [wordComb]
            # print(allCombination)
  return allCombination[len(target)]

print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd","ef","c"]))
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(allConstruct("aaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
# print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee", "eeeeeeeee"]))
