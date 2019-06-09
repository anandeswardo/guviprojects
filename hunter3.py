#anand
num=int(input())
list=[int(i) for i in input().split()]
list2=[]
for i in range(0,num):
    if (list[i]==i):
        list2.append(i)
c=set(list2)
if(len(c)==0):
    print("-1")
else:
    print(*c)
        
