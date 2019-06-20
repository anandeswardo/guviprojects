n=int(input())
li=[int(i) for i in input().split()]
for i in li:
    if li[i]>li[i+1]:
        print(i)
        break
