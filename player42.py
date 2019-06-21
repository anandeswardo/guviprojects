n=int(input())
li=[int(i) for i in input().split()]
li1=sorted(li)
if(li1==li):
    print("yes")
else:
    print("no")
