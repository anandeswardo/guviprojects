n1,n2=map(int,input().split())
li=[]
li1=[]
for i in range(0,n1):
    c,d=map(int,input().split())
    li.append(c)
    li.append(d)
for i in range(len(li)-1):
    for j in range(li[i],li[i+1]+1):
        li1.append(j)
if(n2 in li1):
    print("yes")
else:
    print("no")
