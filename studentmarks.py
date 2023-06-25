#write aprogram to read student and subject marks

marks=[]
m=int(input("enter hw many student"))
n=int(input("enter hw many subject"))

for i in range(m):
    stud=[]
    for j in range(n):
        s=int(input("enter marks"))
        stud.append(s)
    marks.append(stud)


print(marks)
for stud in marks:
    print(stud,sum(stud))
