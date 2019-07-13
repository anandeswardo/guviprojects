n=int(input())
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
li3=[]
for i in li1:
    for j in li2:
        sum=i+j
        li3.append(sum)
        break
print(*li3)
