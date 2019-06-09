#anand
num1,num2=map(int,input().split())
list1=[int(num1) for n in input().split()]
list2=[int(num2) for m in input().split()]
count=0
for i in range(0,len(list2)):
    for j in range(0,len(list1)):
        if list2[i]==list1[j]:
            count+=1
if count==len(list2):
    print("YES")
else:
    print("NO")
