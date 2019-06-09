#anand
num=int(input())
list=[int(i) for i in input().split()]
list2=[]
for i in range(len(list)):
    if(list.count(i)>1):
        list2.append(list[i])
        list2.sort()
print(list2[0])
