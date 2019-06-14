n1,n2=map(int,input().split())
for num in range(n1+1,n2):
  sum=0
  temp=num
  while(temp>0):
    d=temp%10
    sum+=d**3
    temp//=10
  if(num==sum):
    print(num,end=' ')
