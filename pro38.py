n1,n2=map(int,input().split())
li=list(map(int,input().split()))
count=0
for i in li:
	if(i<=(5-n2)):
		count+=1
res=count//3
print(res)
