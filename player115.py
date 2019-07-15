st1,st2=(map(str,input().split()))
st1=list(st1)
st2=list(st2)
if(len(st1)>len(st2)):
  st1=st1[0:len(st2)]
elif(len(st1)<len(st2)):
  st2=st2[0:len(st1)]
for i in range(0,len(st2)):
  st1.append(st2[i])
for i in range(0,len(st1)): 
  print(st1[i],end="")
