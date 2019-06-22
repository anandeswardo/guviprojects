n1,n2=map(int,input().split())
li=[int(i) for i in input().split()]
for i in range(0,len(li)):
    for j in range(i+1,len(li)+1):
        if(li[i]+li[j]==n2):
            print("yes")
            break
else:
    print("no")
