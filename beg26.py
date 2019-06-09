num=int(input())
li=list(map(int,input().list()))
li.sort()
for i in range(len(li)):
    print(*li)
