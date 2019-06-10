num1,num2=map(int,input().split())
list=[int(x) for x in input().split()]
list.sort(reverse=True)
print(list[num2-1])
