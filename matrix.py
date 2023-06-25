matrix=[[1,2],[3,4]]

print(matrix[0],matrix[1])
print(matrix[0][0],matrix[0][1])
print(matrix[1][0],matrix[1][1])

for i in range(2):
    for j in range(2):
        print(matrix[i][j],end='')
    print()

for r in matrix:
    for c in r:
        print(c,end='')
    print()
