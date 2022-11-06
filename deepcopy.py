import copy

a = ["Anand","Virat"]
b = ["Rahul","Sachin"]
res = [a,b]
a[0]=["Kohli"]
#print(a,res)

#copy list
x= ["Rahul","Mahi"]
y=["Sachin","Virat"]
lis = [x,y]
cpy=y[:]
y[0]=["Dhoni"]
#print(cpy,lis)

#deepcopy
s1=["Student 1","Abcd"]
s2=["Student 2","Xyz"]
student=[s1,s2]
student_copy=student[:]
student_copy[0][0] = "Changed"
#print(student_copy)

s3 = copy.deepcopy(student)
student[0][0]=["Bumrah"]
#s3[0][0] = "Changed again"
print(s3)

