n=int(input())
li=list(map(int,input().split()))
a,b=map(int,input().split())
li2=[]
for i in range(n-1):
	for j in range(i+1,n+1):
		c=li[i:j]
		if (c[0]==a and c[-1]==b) or (c[-1]==a and c[0]==b):
			li2.append(len(c))
print(min(li2)-1)
