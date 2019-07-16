n=int(input())
li=list(map(int,input().split()))
pd=1
for i in li:
    pd*=i
if(pd%2==0):
    print("even")
else:
    print("odd")
