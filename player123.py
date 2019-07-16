n=int(input())
li=[]
for i in range(2,n+1):
    c=0
    if(n%i==0):
        for j in range(2,i):
            if(i%j==0):
                c=1
                break
        if(c==0): 
          li.append(i)
print(*li)
