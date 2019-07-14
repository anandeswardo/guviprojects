n=int(input())
li1=[int(x) for x in input().split()]
li2=[]
for i in range(len(li1)-1):
	l=li1[i+1::]
	m=max(l)
	li2.append(m)
li2.append(0)
print(*li2)
