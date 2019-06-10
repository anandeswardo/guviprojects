num=int(input())
list1=[int(i) for i in input().split()]
prod=1
list2=[]
for i in list1:
    prod=prod*i
for i in list1:
    list2.append(prod//i)
print(*list2)
