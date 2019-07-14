n=input()
li=list(map(int,input().split()))
count=0
for i in range(0,len(li)-2):
    for j in range(i+1,len(li)-1):
        for k in range(j+1,len(li)):
            if(li[i]>li[j] and li[j]>li[k]):
                count+=1
print(count)
