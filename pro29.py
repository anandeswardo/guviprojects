n1=int(input())
a=0
b=0
li1=[]
while(a<90 and a<n1):
  s=0
  for j in str(n1-a):
    s+=int(j)
  if s+(n1-a)==n1:
    b+=1
    li1.append(n1-a)
  a+=1
print(b)
for i in li1:
  print(i)
