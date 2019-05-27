n=int(input())
start,end=input().split()
start=int(start)
end=int(end)
if n in range(start+1,end):
    print("yes")
else:
    print("no")
