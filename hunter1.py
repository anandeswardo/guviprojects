n=int(input())
list=[int(i) for i in input().split()]
list1=[]
for i in range (len(list)):
    if(list.count(i)>1):
        list1.append(i)
list1.sort()
print(*list1)
