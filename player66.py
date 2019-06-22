n1,n2=map(int,input().split())
li1=[int(i) for i in input().split()]
count=0
for i in range(0,len(li1)):
    if(li1[i]==n2):
        count+=1
print(count)
