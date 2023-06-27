# write a program to read sales of n years
# and display

n=int(input("Enter value of n"))

#without comprehension

sales=[]
for i in range(n):
    s=float(input("Enter Sale"))
    sales.append(s)
print(sales)

sales=[float(input("Enter Sales")) for i in range(n)]
print(sales)

