n=int(input())
li=list(int(i) for i in str(n))
a=len(li)
li2=list(map(lambda i:i**a,li))
print(sum(li2))
