#anand
st1,st2=map(str,input().split())
count=0
for i in range(0,len(st1)):
    for j in range(0,len(st2)):
        if st1[i]==st2[j]:
            count+=1
if count>=2:
    print("yes")
else:
    print("no")
