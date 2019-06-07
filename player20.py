#anand
str=input()
res=''
for i in str:
    if(i=="X"):
        res+="A"
    elif(i=="Y"):
        res+="B"
    elif(i=="Z"):
        res+="C"
    else:
        res+=chr(ord(i)+3)
print(res)
