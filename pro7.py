n=int(input())
li=[]
a=0
for i in range (0,n+1):
    a=abs((2**i)-n)
    li.append(a)
print(min(li))
