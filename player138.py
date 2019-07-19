n=int(input())
li=[]
for i in range(0,1000):
    if(2**i==n):
        li.append(i)
if(len(li)==0):
    print("no")
else:
    print("yes")
