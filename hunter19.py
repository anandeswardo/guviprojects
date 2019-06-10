#anand
n1,n2=map(int,input().split())
list=[]
for i in range(n1):
    s=set(map(int,input().split()))
    list.append(s)
c=s.intersection(*list)
print(*c)
