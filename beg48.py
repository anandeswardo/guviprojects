n=int(input())
sum=0
list=[int(i) for i in input().split()]
for i in list:
    sum=sum+i
    avg=sum//n
print(avg)
