str=input()
l1=[]
l2=[]
for i in range(0,len(str),2):
    l1.append(str[i])
for i in range(1,len(str),2):    
    l2.append(str[i])
n="".join(map(str,l1))
print(n,end=' ')
print("".join(map(str,l2)))
