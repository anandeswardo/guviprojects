n1,n2=map(int,input().split())
li=[int(i) for i in input().split()]
n3=n1-n2
li2=[]
for i in range(0,n3):
    li2.append(li[i])
print(*li2)
