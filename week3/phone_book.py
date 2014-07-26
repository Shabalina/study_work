import random
import string
alfbt = string.ascii_lowercase
i = 0
f = open('phone_book.txt', 'w')
all_phone = set()
while i != 100000:
    phone = str(random.randrange(10000000))    
    if len(phone)<7:
       phone = "0"*(7-len(phone))+phone
    if phone not in  all_phone:
       name = ""
       for j in range(random.randint(4,10)):
           name = name+random.choice(alfbt)
       all_phone.add(phone)
       f.write(phone +" "+name+"\n")
       i+=1
f.close()       
print ("end")




