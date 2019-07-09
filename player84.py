#anandeswar
n=int(input())
li=list(map(int,input().split()))
s=li[0]
for i in range(1,n):
    s=s | li[i]
print(s)
