from collections import deque, ChainMap, Counter
#Subclass of dict is Counter
print(Counter(['A','B','D','A','B','D','A']))
print(Counter(A=3,B=5,C=4))

de = deque(["Hardik","Virat"])
de.appendleft("Test")
de.append("Ram")
de.pop()
de.popleft()
print(de)

d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
d3 = {'e':5, 'f':5}
c = ChainMap(d1,d2,d3)
print(c.values()," ",c.keys(), " ",c['a'])