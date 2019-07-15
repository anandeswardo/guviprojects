n=int(input())
li=list(map(int,input().split()))
li1=[]
li2=[[li.count(i),i]for i in li]
li2=sorted(li2)
li2=li2[::-1]
for j in li2:
     if(j[1] not in li1):
        li1.append(j[1])
print(*li1)
