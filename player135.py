n=int(input())
li=list(map(int,input().split()))
a=len(li)
if(a%2!=0):
    c=(a-1)//2
    li1,li2=li[0:c],li[c:]
    print(*sorted(li1),end=" ")
    li2=sorted(li2)
    print(*li2[::-1])
else: 
    c=(a)//2
    li1,li2=li[0:c],li[c:]
    print(*sorted(li1),end=" ")
    li2=sorted(li2)
    print(*li2[::-1])
