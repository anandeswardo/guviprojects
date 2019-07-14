n=int(input())
li=[]
su=0
for i in range(n):
  li.append(list(map(int,input().split())))
for i in li:
  su+=sum(i)
print("{0:2f}".format((su/(n*n))))
