n=int(input())
li1=list(map(int,input().split()))
li1.sort()
a=0
b=0
for i in range(len(li1)):
    if li1[i]>=a:
        b=b+1
    a=a+li1[i]
print(b)
