num=int(input())
li=[int(i) for i in input().split()]
for i in range(len(li)):
    li.sort()
print(*li)
