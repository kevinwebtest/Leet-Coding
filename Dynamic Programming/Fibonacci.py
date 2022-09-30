def fib2(n):
  fibo = [0 for i in range(n+3)]
  fibo[1] = 1
  for num in range(n+1):
    fibo[num+1] += fibo[num]
    fibo[num+2] += fibo[num]
  return fibo[n]
print(fib2(50))

def fib(n, memo={}):
  if n in memo:
    return memo[n]
  if n==0:
    return 0
  if n==1:
    return 1
  memo[n] = fib(n-1)+fib(n-2)
  return memo[n]

print(fib(50))
