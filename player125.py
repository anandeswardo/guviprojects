n=int(input())
li=list(map(int,input().split()))
li1=[]
for i in range(1,max(li)+1):
    c=0
    for j in range(0,n):
        if(li[j]%i==0):
            c=c+1
        if(c==n):
             li1.append(i)
print(max(li1))
