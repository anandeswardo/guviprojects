#anand
n,k=map(int,input().split())
k=k%n
list1=[int(i) for i in input().split()]
list2=list1[-k:]+list1[:-k]
print(*list2)
