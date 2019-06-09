#anand
from itertools import permutations
ls1=list(input())
per1=permutations(ls1)
a=[]
for i in list(per1):
    s=''
    for j in i:
       s+=j
    if s not in b:
       a.append(s)
       print(s)
