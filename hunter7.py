#anand
num=int(input())
list=[int(i) for i in input().split()]
for i in list:
    if list.count(i)>1:
        print(i)
        break
else:
    print("unique")
