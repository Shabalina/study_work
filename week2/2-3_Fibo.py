

def fibo(n):
  print("Start to calculate Fibonacci number for %d" % n)
  if n <2 0: return n
  else: result = fibo(n - 1) + fibo(n - 2)
  print("The sum of Fibonacci numbers for  %d and %d equal to %d" % (n-1, n-2, result))
  return result


 
print (fibo(6))
