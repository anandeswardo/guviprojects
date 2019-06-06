#anand
n=int(input())
count=0
list=[int(i) for i in input().split()]
for j in list:
    if(list.count(j)==1):
        print(j)
