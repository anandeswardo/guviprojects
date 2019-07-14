st=input()
a=0
for i in range(0,len(st)):
    sv=st[0:i]+st[i+1::]
    if(int(sv)%8==0):
        a=1
        break
if(a==1):
    print("yes")
else:
    print("no")
