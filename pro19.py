n=int(input())
li=[]
li2=[]
for i in range(n):
    li.append(input().split())
for x in li:
    for y in x:
        li2.append(int(y))
for i in sorted(li2):
    print(i,end=' ')
