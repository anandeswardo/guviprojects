n=int(input())
li=list(map(int,input().split()))
li=[bin(x) for x in li]
li.sort(reverse=True)
li=[int(x,2) for x in li]
for i in li:
    print(i)
