#anand
n=int(input())
li=[int(i) for i in input().split()]
a=li[0]
for i in range(1,n):
    a=a^li[i]
print(a)
