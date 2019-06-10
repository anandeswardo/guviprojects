n1,n2=map(int,input().split())
list=[int(x) for x in input().split()]
count=0
for i in range(0,n1):
    for j in range(i+1,n1):
        s=list[i]+list[j]
        if(s==n2):
            count+=1
if(count>=1):
    print("YES")
else:
    print("NO")
