def first_last(target, numbers):
  for i in range(len(numbers)):
    if numbers[i]==target:
      start = i
      while numbers[i+1]==target:
        i+=1
      return [start,i]
  return [-1,-1]

print(first_last(0,[2,3,5,5,5,5,5,7,8,9])) # 2,6
