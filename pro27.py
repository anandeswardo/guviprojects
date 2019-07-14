#anand
n1,n2=map(int,input().split())
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
li3=[]
a=0
for i in range(n1):
    x=li2[i]/li1[i]
    li3.append(x)
while(n2>=0 and len(li3)>0):
    mindex=li3.index(max(li3))
    if(n2>=li1[mindex]):
        a=a+li2[mindex]
        n2=n2-li1[mindex]
    li1.pop(mindex)
    li2.pop(mindex)
    li3.pop(mindex)
print(a)
