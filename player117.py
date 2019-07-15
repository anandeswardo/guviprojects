li=list(map(str,input()))
li=li[::-1]
for i in range(0,len(li)):
    if(i==len(li)-1): 
      print(li[i])
    else: 
      print(li[i],end="-")
