n=int(input())
li=input().split()
li2=[]
for i in range(n):
    s=li[i]
    for j in range(i+1,n):
        if(int(li[i])<int(li[j]))and (int(li[j-1])<int(li[j])):
            s+=li[j]
        else:
            break
    li2.append(len(s))
print(max(li2))
