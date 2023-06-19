#write program to check the last digit
#check the entered number is divisible by 3 or not
num=int(input("enter the value"))
lastDig=num%10
if lastDig%3==0:
    print(f'last digit of {num} is divisible by 3')
else:
    print(f'last digit of {num} is not divisible by 3')

