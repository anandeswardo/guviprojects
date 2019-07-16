n,k=map(int,input().split())
li=list(map(int,input().split()))
li1=[]
for i in li:
    if(li.count(i)<k):
        li1.append(i)
print(*sorted(set(li1)))
