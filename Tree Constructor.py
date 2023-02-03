import re
def TreeConstructor(strArr):
  parents = {}
  children = {}
  for nodes in strArr:
    c,p = re.findall("[0-9]+",nodes)
    if p not in parents:
      parents[p]=[]
    parents[p].append(c)
    if len(parents[p])>2:
      return False
    if c not in children:
      children[c] = p
    else:
      return False
  return True
