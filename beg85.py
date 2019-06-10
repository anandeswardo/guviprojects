st=input()
l1=[]
l2=[]
for i in range(0,len(st),2):
    l1.append(st[i])
for i in range(1,len(st),2):    
    l2.append(st[i])
n="".join(map(str,l1))
print(n,end=' ')
print("".join(map(str,l2)))
