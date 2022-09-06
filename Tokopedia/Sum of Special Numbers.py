def isPrimee(n):
  for it in range(2,n//2+1):
    if n%it==0:
      return False
  return True

def checkNumbers(number):
  output = 0
  for i in range(2, number+1):
    primeNum=isPrimee(i)
    if primeNum==True or i%6==0:
      continue
    output += i
  return output

print(checkNumbers(15))
