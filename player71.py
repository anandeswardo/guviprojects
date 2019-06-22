n=int(input())
li=[int(i) for i in input().split()]
for i in range(n-1):
    if(li[i]<li[i+1]):
        print(li[i+1],end=" ")
    else:
        print(li[i],end=" ")
