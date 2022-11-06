
def add(val1,val2):
    return val1+val2


num1 = [5,10,15,20]
num2 = [5,10,20,30]
res = map(add,num1,num2)
print(list(res))

