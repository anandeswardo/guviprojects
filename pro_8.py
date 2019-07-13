import math
n1,n2=map(int,input().split())
li1=[]
li2=list(map(int,input().split()))
for i in range(0,n2):
    a,b=map(int,input().split())
    li1.append([a,b])
for i in li1:
    c=i[0]-1
    d=i[1]-1
    print(math.gcd(li2[c],li2[d]))
