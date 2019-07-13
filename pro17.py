n1,n2=map(int,input().split())
li=list(map(int,input().split()))
a=0
for i in range(0,len(li)):
    for j in range(i,len(li)):
        if(li[i]+li[j]==n2):
            a=1 
            break
    if(a==1):
        break
if(a==0):
    print("no")
else:
    print("yes")
