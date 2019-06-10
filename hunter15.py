#anand
n=int(input())
list=[int(x) for x in input().split()]
s=[]
for i in range(0,len(list)):
    l1=list[i:]
    m=max(l1)
    if list[i]==m:
        s.append(list[i])
print(*s)
print(max(list))
