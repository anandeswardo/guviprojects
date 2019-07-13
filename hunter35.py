st=input()
n=0
for i in range(len(st)):
    if(st[:i]==st[i+1:]):
        n=0
        break
    else:
        n=1
if(n==0):
    print("YES")
else:
    print("NO")
