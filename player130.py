n1=int(input())
li=[int(x) for x in input().split()]
li1=[]
for i in range(n1):
    c=li[:i+1]
    if(sum(c)%2==0):
        li1.append(str(sum(c)))
    else:
        li1.append(str(li[i]))
print(" ".join(li1))
