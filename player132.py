st=str(input())
li=[]
c=0 
m=0
for i in range(len(st)-1):
    m=int(st[i])+int(st[i+1]) 
    if(m%2!=0):
        c=c+1 
    else:
        li.append(c)
        c=0
    li.append(c)
c1=max(li)
if(c1==0):
    print("0")
else:
    print(c1+1)
