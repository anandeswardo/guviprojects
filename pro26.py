n=int(input())
li=list(map(int,input().split()))
li2=[]
s=1
for i in li:
  if i not in li2:
    li2.append(i)
for i in range(len(li2)-1):
  if (li2[i]<li2[i+1]):
    s+=1
print(s)
