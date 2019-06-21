n1,n2=map(str,input().split())
n=list(n1)
count=0
for i in range(0,len(n)):
    if(n2==n[i]):
        count=count+1
print(count)
