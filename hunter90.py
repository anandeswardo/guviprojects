st=input()
c=0
k=st[0]
m=0
hi=""
for i in range(len(st)-1):
    if(st[i]==k):
        c=c+1
    if st[i]!=st[i+1]:
        if(c>m):
            m=c
            hi=st[i]
        c=0
        k=st[i+1]
    if i+1==len(st)-1 :
        if(c+1>m):
            m=c+1
            hi=st[i]
        
print(hi,end=" ")
print(m,end="")
