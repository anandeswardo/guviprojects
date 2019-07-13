n1=int(input())
li1=list(map(int,input().split()))
a1=li1
li2=[]
while(len(a1)!=1):
    for i1 in range(len(a1)):
        if i1%2!=0:
            li2.append(a1[i1])
    a1=li2
    li2=[]
print(li1.index(a1[0]))
