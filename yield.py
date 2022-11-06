def add(num):
    yield num+1

val1 = add(5)
print(next(val1))



def sub(num):
    yield num -1

val2 = sub(5)
print(next(val2))

