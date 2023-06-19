#program to find input character
#check alphabate digit or specialcharacter
ch=input("enter any character")
if(ch>='A' and ch<='Z')or(ch>='a' and ch<='z'):
    print(f'{ch} is aplphabet')
elif ch>='0' and ch<='9':
    print(f'{ch} is digit')
else:
    print(f'{ch} is special')
