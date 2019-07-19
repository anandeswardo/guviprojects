n=int(input())
li=list(map(int,input().split()))
a=0
b=0
li.sort(reverse=True)
for i in li:
  li=a+i
  if b>li:
    a=li
  else:
    a=b
    b=li
print(a,b)
