#write a program to print 1 to 10

for i in range(10): # start=0,stop=10,step=1
    for num in range(1,6):
        print(num,end='')
    print()
print()


#write a program to generate tables from 1 to 10

for num in range(1,11):
    for i in range(1,11):
        p=num*i
        print(f'{num}x{i}={p}')
    input()
print()

