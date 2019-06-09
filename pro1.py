#anand
num=int(input())
list=[]
for j in range(0,num):  
    n1=input()
    list.append(n1)
f1=[]
for j in zip(*list):
    if j.count(j[0])==len(j): 
        f1.append(j[0])
    else:
        break
print(''.join(f1))
