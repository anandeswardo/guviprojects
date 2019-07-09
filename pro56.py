#anand
n,t=map(int,input().split())
sec=list(map(int,input().split()))
c=0
for i in sec:
  t1=86400-i
  t=t-t1
  c+=1
  if t<=0:
    break  
print(c)
