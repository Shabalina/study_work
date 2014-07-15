import math
def maximum_prime(integer):
    num = 2
    loop = True
    while loop == True:
          while integer%num == 0:
                integer = integer//num
                if integer ==1:
                   max_prime = num
                   loop = False
                   break          
          num += 1
          if loop == True and math.sqrt(integer) < num:
             max_prime = integer 
             loop = False
    return max_prime

print (maximum_prime(7786543297))


 
