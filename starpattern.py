space=5
for i in range(1,7):
    for s in range(space):
        print(' ',end='')
    space=space-1
    for j in range(1,i+1):
        print('* ',end='')
    print()
print()

space=5
for i in range(1,7):
    for s in range(space):
        print('* ',end=' ')
    space=space-1
    for j in range(1,i+1):
        print(' ',end=' ')
    print()
print()
    
space=0
for i in range(7,0,-1):
    for s in range(space):
        print(' ',end=' ')
    space=space+1
    for j in range(1,i+1):
        print('*',end=' ')
    print()
print()


space=4
for i in range(5,0,-1):
    for s in range(space):
        print(' ',end=' ')
    space=space-1
    for j in range(1,i+1):
        print('* ',end=' ')
    print()
