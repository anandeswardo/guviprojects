a,b=map(int,input().split())
list=[]
for i in range(a,b+1):
    if(a%i==0 and b%i==0):
        list.append(i)
print(max(list))
