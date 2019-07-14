st=input()
a=st.count("@")
b=st.count(".")
for i in range(len(st)-2):
	if(st[i]=="@"):
		x=st[:i]
		c=i
	if(st[i]=="."):
		y=st[c+1:i]
if(a==1 and b==1 and len(x)>=3 and len(y)<=5 and st[len(st)-4:]==".com"):
	print("YES")
else:
	print("NO")
