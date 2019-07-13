from itertools import combinations
st=input()
n=0
li=list(combinations(st,len(st)-1))
for i in range(len(li)):
    if(li[i]==li[i][::-1]):
        print("YES")
        n=1
        break
if(n==0):
    print("NO")
