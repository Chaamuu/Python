for i in range(1,6):
    for j in range(1,6):
        if j>=i:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
print()

for i in range(1,6):
    for j in range(5,0,-1):
        if j<=i:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
print()

num=1
for i in range(1,6):
    for j in range(1,i+1):
        print(num,end=' ')
        num=num+1
    print()
