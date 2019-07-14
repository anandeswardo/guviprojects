st=input()
st2=""
a=0
for i in range(len(st)-1):
    st2=""
    if(st[i]==st[i+1]):
        st2=st2+st[:i+1]+st[i+2:]
        if(int(st2)>a):
            a=int(st2)
print(a)
