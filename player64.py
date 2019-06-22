n1,n2=map(int,input().split())
li1=[int(i) for i in input().split()]
li2=[]
for i in range(0,len(li1)):
    if(li1[i]<n2):
        li2.append(li1[i])
li2.sort()
print(*li2)
