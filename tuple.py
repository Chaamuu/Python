test_list=[(5,36),(37,9)]
list1=[]
for t in test_list:
    list1.extend(t)

print(list1)
output=[]
for value in list1:
    output.extend(str(value))

output=list(map(int,output))
print(output)
