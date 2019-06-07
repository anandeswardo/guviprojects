a,b=map(int,input().split())
s1=input()
list1=[int(i) for i in input().split()]
list2=[int(i) for i in input().split()]
list3=[]
for i in range(len(list2)):
    list1.append(list2[i])
    s=max(list1)
    list3.append(s)
print(*list3)
