num=int(input())
a=[int(i) for i in input().split()]
b=[]
c=[]
for j in range(0,len(a)):
    if(j%2==0):
        b.append(a[j])
    else:
        c.append(a[j])
for k in b:
    d=sum(b)
for l in c:
    e=sum(c)
if(d>e):
    print(d)
else:
    print(e)
