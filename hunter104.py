n=int(input())
su=0
b=str(n)
li=[]
for i in range(0,len(b)):
    su=su+int(b[i])
    li.append(su)
print(sum(li))
