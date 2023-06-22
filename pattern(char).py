for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=' ')
    print()
print()

for i in range(65,70):
    for j in range(65,70):
        print(chr(j),end=' ')
    print()
print()

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end=' ')
    print()
print()

for i in range(65,70):
    for j in range(65,70):
        if j>=i:
            print(chr(i),end=' ')
        else:
            print(' ',end=' ')
    print()
print()

for i in range(65,70):
    for j in range(65,i+1):
        if j>=i:
            print(chr(i),end=' ')
        else:
            print(' ',end=' ')
    print()
print()
