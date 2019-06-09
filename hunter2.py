num=int(input())
list=[int(i) for i in input().split()]
list.sort(reverse=True)
for i in range (len(list)):
    print(list[i],end='')
