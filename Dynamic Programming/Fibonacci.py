# Recursive version
def fib(n, memo={}):
  if n in memo:
    return memo[n]
  if n==0:
    return 0
  if n==1:
    return 1
  memo[n] = fib(n-1,memo)+fib(n-2,memo)
  return memo[n]
print(fib(50)) #12586269025

# Tabular version
def fib2(n):
  fibo = [0 for i in range(n+3)]
  fibo[1] = 1
  for num in range(n+1):
    fibo[num+1] += fibo[num]
    fibo[num+2] += fibo[num]
  return fibo[n]
print(fib2(50))


def fib3(n):
  if n==0:
    return 0
  results=[0,1]
  res = 0
  for i in range(n-1):
    res = results[i]+results[i+1]
    results.append(res)
  return results[n]

print(fib3(50))#12586269025

# i=0 -> res[2]=1
# i=1 -> res[3]=2
# i=2 -> res[4]=3
# i=3 -> res[5]=5