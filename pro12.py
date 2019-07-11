n1,n2=map(int, input().split())
li=list(map(int, input().split()))
li2=[]
for _ in range(n2):
    a,b=map(int, input().split())
    li2.append(sum(li[a-1:b]))
for i in li2:
    print(i)
