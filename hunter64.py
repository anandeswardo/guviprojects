n=int(input())
li=[1000,500,100,50,10,1]
c=0
while(n>0):
    for i in range(0,len(li)):
        if(n>=li[i]):
            n=n-li[i]
            c+=1
            break
print(c)
