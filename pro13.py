n1,n2=[int(i) for i in input().split()]
li1=[]
li2=[int(i) for i in input().split()]
for _ in range(n2):
    a,b=[int(i) for i in input().split()]
    li1.append(min(li2[a-1:b]))
for i in li1:
    print(i)
