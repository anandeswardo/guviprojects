n1=input()
li=list(set(n1))
x1=1
a1=0
check=False
while(True):
    ch=li[a1]
    for y in range(0,len(n1)-x1):
        if(ch in n1[y:y+x1]):
            check=True
        else:
            check=False
            a1=a1+1
            if(a1>=len(li)):
             a1=0
             x1=x1+1
            break
    if(check==True):
        break
print(x1)
