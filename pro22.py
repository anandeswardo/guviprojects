num=int(input())
a=[int(i) for i in input().split()]
b=[]
c=[]
for j in range(0,len(a),2):
    b.append(a[j])
for j in range(1,len(a),2):    
    c.append(a[j])
for k in b:
    d=sum(b)
for l in c:
    e=sum(c)
if(d>e):
    print(d)
else:
    print(e)
