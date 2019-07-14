n1,n2=map(int,input().split())
li=list(map(int,input().split()))
while n2 in li:
    li.remove(n2)
if not li:
    print("empty")
else:
    print(*li)
