#create 2x2 matrix and display

matrix=[]

for i in range(2):
    row=[]
    for j in range(2):
        x=int(input("enter value"))
        row.append(x)
    matrix.append(row)

print(matrix)
