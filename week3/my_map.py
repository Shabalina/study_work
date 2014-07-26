
def dummy_func (a,b):
    print (a, b)
    c = a+2*b
    return str(c)


def my_map (func, *seq):
    tuple_seq = zip(*seq)
    for arg in tuple_seq:
        yield func(*arg)
        


a = {'o','m','r','a'}
b = ['a','r','o','m']

print(list(my_map(dummy_func, a, b)))




