n=int(input())
li=[]
x=0
for i in range(2,n):
    for j in range(2,i+1):
        if(i%j==0):
            break
    if(j==i):
        li.append(i)
for i in range(len(li)):
    for j in range(len(li)):
        for k in range(len(li)):
            if(li[i]+li[j]+li[k]==n):
                print(str(li[i])+" "+str(li[j])+" "+str(li[k]))
                x=1
                break
        if(x==1):
            break
    if(x==1):
        break
