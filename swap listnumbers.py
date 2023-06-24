n=int(input("how many values"))
list1=[]

for i in range(n):
    values=input("enter value")
    list1.append(values)

print(f'before swapping{list1}')
pos1=int(input("enter position 1"))
pos2=int(input("enter position 2"))
list1[pos1-1],list1[pos2-1]=list1[pos2-1],list1[pos1-1]
print(f'after swapping{list1}')
