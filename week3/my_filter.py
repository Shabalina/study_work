
def dummy_func (a):
    print (a)
    return a in "!!yellow elephant!!"


def my_filter (func, seq):
    iter_seq = list(seq)    
    return (arg for arg in iter_seq if func(arg)==True)
        


a = ['p','m','z','y','r','t','i','s','h','o','v','n','k']

print (my_filter(dummy_func, a))

print (filter(dummy_func, a))



