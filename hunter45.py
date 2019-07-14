n=int(input())
li=[int(i) for i in input().split()]
c=0
for i in range(0,n+1):
    if n*i in li:
        c=c+1
print(c) 
