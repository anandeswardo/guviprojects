n1,n2=map(int,input().split())
li1=[int(i) for i in input().split()]
li2=[int(i) for i in input().split()]
for i in range(len(li2)):
    li1.append(li2[i])
li1.sort()
print(*li1)
