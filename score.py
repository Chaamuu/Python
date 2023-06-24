n=int(input("enter how many players"))
scores=[]
for i in range(n):
    s=int(input("enter scores"))
    scores.append(s)

print(f'scores are{scores}')
print(f'maximum score{max(scores)}')
print(f'minimum score{min(scores)}')
print(f'total score {sum(scores)}')
