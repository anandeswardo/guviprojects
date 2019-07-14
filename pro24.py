from itertools import permutations,combinations_with_replacement
n=int(input())
li1=[]
li2=[]
com=combinations_with_replacement(['0','1'], n)
for i in list(com):
    p=permutations(list(i))
    for i in list(p):
        x=("".join(i))
        if x not in li1:
            li1.append(x)
            print(x)
