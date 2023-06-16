ch=input("enter any character")
if ch>'A' and ch<='Z':
	ch=chr(ord(ch)+32)
	print(f'Lowercase character {ch}')
elif ch>='a' and ch<='z':
	ch=chr(ord(ch)-32)
	print(f'Uppercase character{ch}')
else:
	print("input only alphabets")
