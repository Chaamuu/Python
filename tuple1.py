#Return a new sorted list from the items in iterable.
test_tup = (3, 7, 1, 18, 9)
s=sorted(test_tup)
print(s)
k=2
min_e=s[:2]
max_e=s[-2:]
res_t=tuple(min_e+max_e)
print(res_t)
