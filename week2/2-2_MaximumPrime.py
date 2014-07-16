import math
def maximum_prime(integer):
    num = 2
    while True:
          if integer%num == 0:
             integer = integer/num
             if integer ==1:
                 max_prime = num
                 break
          else:     
             if num == 2: num = 3
             else: num += 2
             if math.sqrt(integer) < num:
                max_prime = integer
                break
    return max_prime

print (maximum_prime(1))


 
