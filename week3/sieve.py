
def sieve(integer):
    if integer <= 1:
       return [1]
    divisor = 2
    total = 0
    prime = list(range(2, integer+1))
    while divisor < prime[-1]:
         temp = []
         for num in prime[total:]:
             if (num%divisor != 0 or
                 num/divisor == 1.0):
                 temp.append(num)
         prime = list(prime[:total]) + list(temp)
         total += 1
         divisor = prime[total]
         
    return prime


test = [7,10,11,17,1024,45,67,28,1,117,2]
for el in test:
    print (el, sieve(el))
