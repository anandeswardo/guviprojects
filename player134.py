n1,n2,n3=map(int,input().split())
li=list(map(int,input().split()))
li1=[]
for i in range(n2-1,n3):
    li1.append(li[i])
print(min(li1)) 
