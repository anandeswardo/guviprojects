n1,n2=map(int,input().split())
li=list(map(int,input().split()))
if(n2 in li):
    print("yes",end=" ")
    print(li.count(n2))
else:
    print("no")
