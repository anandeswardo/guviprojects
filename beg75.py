st=list(input())
if len(st)%2==0:
    st[int(len(st)/2)] ='*'
    st[int(len(st)/2)-1]='*'
else:
    st[int(len(st)/2)] ='*'
for i in range(0,len(st)):
    print(st[i],end='')
