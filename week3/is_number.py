

def is_number(string):
    if len(string) == 0: return False
    sign_count = 0
    dot_count = 0
    digit_count = 0
    sign_place = 0
    first_digit = 1
    min_digit = 0
    for char in range(len(string)):
        if string[char] == "-" or string[char] == "+":
           sign_count += 1
           sign_place = char
        if string[char] == ".":
           dot_count += 1
        if string[char].isdigit():
           digit_count += 1
           if digit_count == 1:
              first_digit = int(string[char])
           if int(string[char]) > min_digit:
              min_digit =  int(string[char])
    if (len(string)>(sign_count+dot_count+digit_count)
        or sign_count > 1
        or dot_count >1
        or sign_place != 0
        or dot_count == 0 and first_digit == 0 and min_digit > 0):
        return False
    return True  

test = (["3!56","0.2-0","--76","-000000008","+0.0000007","0","0.2.37","987.6",
         "-.7","","-0000","456.","1"])              
for trial in test:
    print (trial, is_number(trial))


