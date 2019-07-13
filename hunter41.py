n=int(input())
li1=[int(i) for i in input().split()]
li2=[]
for i in range(0,n):
    a=1
    for j in range(i,n):
        a=a*li1[j]
    li2.append(a)
for i in range(0,n):
    a=1
    for j in range(i+1):
        a=a*li1[j]
    li2.append(a)
print(max(li2))
