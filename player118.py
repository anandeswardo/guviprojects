li=[str(i) for i in input().split()]
a=0
res=""
for i in li:
    if(a<len(i)):
        res=i
        a=len(i)
print(res)
