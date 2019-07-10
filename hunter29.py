#anand
n1=int(input())
l1=list(map(int,input().split()))
l2=[]
for i1 in range(n1-1):
    for j1 in range(i1,n1):
        c1=l1[i1:j1+1]
        l2.append(sum(c1))
print(max(l2))
