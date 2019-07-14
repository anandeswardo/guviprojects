li1=list(map(str,input().split()))
li1[len(li1)-1]=li1[len(li1)-1].replace(".","")
for i in range(len(li1)):
  if i%2==0:
    li1[i]=li1[i][::-1]
print(*li1)
