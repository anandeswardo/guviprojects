str=input()
res=''
for i in str:
    res+=chr(ord(i)+3)
print(res,end='')
