n=int(input())
su=0
while(n!=0):
  i=n%10
  su=su+i**2
  n=n//10
print(su)
