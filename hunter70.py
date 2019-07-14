from itertools import combinations
n1,n2,n3=map(int,input().split())
li=list(map(int,input().split()))
c=0
a=list(combinations(li,n2))
for i in range(len(a)):
	if(sum(a[i])==n3):
		c=1
		print("YES")
		break
if(c==0):
	print("NO")
