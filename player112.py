num=int(input())
li1=list(map(int,input().split()))
li2=[]
for i in range(len(li1)+1):
    for j in range(i+1,len(li1)+1):
        li2.append(li1[i:j])
print(len(li2)) 
