import math
n1,n2=input().split()
n1=int(n1)
n2=int(n2)
num=n1*n2
root=math.sqrt(num)
if(int(root+0.5)**2==num):
    print("yes")
else:
    print("no")
