n=int(input())
li=[int(x) for x in input().split()]
li1=[0]
for i in range(n):
    for j in range(i,n):
        l=li[i:j+1]
        li1.append(sum(l))
print(min(li1))
