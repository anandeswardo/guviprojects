#anand
n=0
n1=0
st=input()
li=[]
for i in st:
  if i not in li:
    li.append(i)
    n1+=1
    if n<n1:
       n=n1
  else:
    n1=0
print(n)
