n=int(input())
start,end=input().split()
if n in range(int(start+1),int(end)):
    print("yes")
else:
    print("no")
