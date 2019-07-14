li1=list(map(str,input().split("#")))
li2=list(map(str,input().split("#")))
li3=list(int(li1[i]) for i in range(1,len(li1)))
li4=list(int(li2[i]) for i in range(1,len(li2)))
s1=sum(li3)
s2=sum(li4)
if(s1>s2):
	print(li1[0])
else:
	print(li2[0])
