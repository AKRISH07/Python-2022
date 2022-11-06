#%time v = [ i**2 for i in range(1,10000)]
#%time g = (i**2 for i in range(1,10000))

res = (x**2 for x in range(1,100) if x%2 == 0)
print(next(res))
print(next(res))