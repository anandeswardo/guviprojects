n=int(input())
li=[]
sum=0
for i in range(n):
  li.append(list(map(int,input().split())))
for i in li:
  sum+=sum(i)
print("{0:2f}".format((sum/(n*n))))
