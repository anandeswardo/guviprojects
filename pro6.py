n1=int(input())
li=list(map(int,input().split()))
n3=0
for i in range(n1):
    for j in range(i,n1):  
        for k in range(j,n1):
            if li[i]<li[j]<li[k]:
                n3+=1
print(n3)
