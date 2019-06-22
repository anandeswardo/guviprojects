n1=int(input())
li1=[int(i) for i in input().split()]
li2=[]
for i in range(0,len(li1)):
    if(li1[i]<n1):
        li2.append(li1[i])
print(*li2)
