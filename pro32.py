#anand
n1,n2=map(int,input().split())
if(n1<=n2):
    d=n1
else:
    d=n2
l=[]
for i in range(0,d):
    l.append(sorted(list(map(int,input().split()))))
l=sorted(l)
for i in range(0,len(l[0])):
    for j in range(0,len(l)-1):
        if(l[j][i]>l[j+1][i]):
            l[j][i],l[j+1][i]=l[j+1][i],l[j][i]
for i in l:
  print(*i)
