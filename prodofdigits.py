n=int(input())
prod=1
while(n>0):
    r=n%10
    prod=prod*r
    n=n//10
print(prod)
