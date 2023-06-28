list=[10,60,30,20,45,67,89]

c=0
for value in list:
    c=c+1

print(f'length of list is {c}')
print()


#check element exists in list

emails=["mahesh@gamil.com",
        "suresh@gmail.com",
        "nagesh@gmail.com",
        "radhika@gmail.com"]

email=input("enter email-id which u want to find")

if email in emails:
    print(f'{email} found')
else:
    print(f'{email} not found')
