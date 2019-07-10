#anand
from itertools import permutations
n=input()
li=[]
a=permutations(n)
for i in a:
    b=int("".join(i))
    if b>int(n):
        li.append(int("".join(i)))
print(min(li))
