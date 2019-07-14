n=input()
s=input().split()
count=0
p=input()
for i in s:
	if(p==i[:len(p)]):
		count+=1
print(count)
