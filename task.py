import itertools 
s = list(input())
perm_set= itertools.permutations(s) 
for val in perm_set: 
    print(''.join(val))