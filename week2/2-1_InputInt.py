
def input_int(lo, hi):
     print ("Please enter integer type value "
                  "from %d to %d" % (lo, hi))
     while True:
          user_input = input()
          if user_input.isdigit() == False:
             print ("Your input has wrong type,"
                  " please enter only integer type value")
          elif int(user_input) < lo or int(user_input) > hi:
             print ("Your input is wrong, please enter integer "
                  "from %d to %d" % (lo, hi))
          else:
             break
             
     return user_input + ' is correct'
                  


print (input_int(100, 200))
