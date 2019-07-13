n=int(input())
li=list(map(int,input().split()))
sum=0
for i in range(1,len(li)):
    for j in li[:i]:
        if j<li[i]:
            sum+=j
print(sum)
