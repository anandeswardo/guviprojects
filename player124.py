n=int(input())
li1=list(map(int,input().split()))
li2=[]
li3=[]
for i in range(1,1000):
    for j in li1:
        if(i%j==0):
            li2.append(i)
    if(li2.count(i)==n):
        li3.append(i)
print(li3[0])
