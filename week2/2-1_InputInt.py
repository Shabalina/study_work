
def input_int(lo, hi):
     print ("Please enter integer type value "
                  "from %d to %d" % (lo, hi))
     user_input = input()
     while True:
          if user_input.isdigit() == False:
             print ("Your input has wrong type,"
                  " please enter only integer type value")
             user_input = input()
          elif int(user_input) < lo or int(user_input) > hi:
             print ("Your input is wrong, please enter integer "
                  "from %d to %d" % (lo, hi))
             user_input = input()
          else:
             break
             
     return "Input accepted"
                  


print (input_int(100, 200))
