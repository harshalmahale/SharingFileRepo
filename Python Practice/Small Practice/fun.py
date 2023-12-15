# def add(a,b):
    # return a + b


def new_add(*values):
    total = 0
    for num in values:
        total += num
    return total

print(new_add(1,2,3,4))

def fun2(name,*args,last_name = 'unknown',**krgs):
    print(name)
    print(args)
    print(last_name)
    print(krgs)
fun2('Keechu', 1,2,3, a=1 , b=2)
