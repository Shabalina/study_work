
def fib(intgr):
    x = 0
    y = 1
    if intgr < 2: return intgr
    for i in range(intgr-1):
        fib_num = x+y
        x = y
        y = fib_num
    return fib_num
 
print (fib(6))
