import time
import random



def dic_get_name(phone):
    book = {}
    f = open('phone_book.txt', 'r')
    for line in f:
        rec = line.strip().split(" ")
        book[rec[0]] = rec[1]
    f.close    
    zero = time.clock()
    name = book.get(phone)
    timing = time.clock()- zero
    return name, timing

def list_get_name(phone):
    book = []
    f = open('phone_book.txt', 'r')
    for line in f:
        book.append(tuple(line.strip().split(" ")))
    f.close()
    zero = time.clock()
    name = str([x[1] for x in book if x[0] == phone]).strip('[]')
    timing = time.clock()- zero
    return name, timing

def search(phone, book):
"""binary search"""
    if len(book)%2 == 0: indx =  len(book)//2-1
    else: indx =  len(book)//2
    if int(book[indx][0]) == phone:
       return book[indx][1]
    if int(book[indx][0]) > phone:
       return search(phone, book[:indx])
    else:       
       return search(phone, book[indx+1:])

def sortlist_get_name(phone):
    book = []
    f = open('phone_book.txt', 'r')
    for line in f:
        book.append(tuple(line.strip().split(" ")))
    f.close()
    book.sort(key=lambda x: x[0])
    zero = time.clock()
    name = search(int(phone), book)
    timing = time.clock()- zero
    return name, timing

book = []
f = open('phone_book.txt', 'r')
for line in f:
    book.append(tuple(line.strip().split(" ")))
print ("pass")
dic_time = 0
list_time = 0
sortlist_time = 0
for i in range(2):
    pair = random.choice(book)
    name, timing = dic_get_name(pair[0])
    dic_time += timing
    print(name)
    name, timing = list_get_name(pair[0])
    list_time += timing
    print(name)
    name, timing = sortlist_get_name(pair[0])
    sortlist_time += timing
    print(name)
    

print ("dictionary: "+ str(dic_time) +"\n",
       "list: "+ str(list_time)+"\n",
       "sort list: "+ str(sortlist_time))

# быстрее поиск по словарю т.к. это множество, не надо перебирать индексы
# время поиска по несортированому словарю линейно зависит от индекса
#нужного элемента, чем дальше от начала тем дольше
#время бинарного поиска растет логарифмично
    
