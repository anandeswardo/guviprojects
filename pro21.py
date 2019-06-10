#anand
num=int(input())
list=[int(x) for x in input().split()]
av=int(num/2)
l1=list[:av]
l2=list[av::]
n1=sum(l1)//len(l1)
n2=sum(l2)//len(l2)
if(n1==n2):
    print("yes")
else:
    print("no")
